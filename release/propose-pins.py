#!/usr/bin/env python3
"""Propose updated upstream pins for awx-platform-images.

Fetches default branch tip (and optionally latest semver tags) from GitHub
without cloning full repos. Writes pins.proposed.yaml for human/agent review.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


def load_pins(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if yaml:
        return yaml.safe_load(text)
    # minimal fallback: not full YAML; require pyyaml in CI
    raise SystemExit("PyYAML required: pip install pyyaml")


def dump_pins(data: dict, path: Path) -> None:
    if not yaml:
        raise SystemExit("PyYAML required")
    path.write_text(
        yaml.safe_dump(data, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )


def github_api(url: str, token: str | None) -> dict | list:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "awx-platform-images-propose-pins")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def parse_github_repo(repo_url: str) -> tuple[str, str]:
    # https://github.com/ansible/awx.git → ansible, awx
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", repo_url)
    if not m:
        raise ValueError(f"Not a GitHub URL: {repo_url}")
    return m.group(1), m.group(2)


def resolve_ref(owner: str, repo: str, ref: str, token: str | None) -> str:
    """Return commit SHA for branch or tag."""
    # Try commit directly
    try:
        data = github_api(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{ref}",
            token,
        )
        if isinstance(data, dict) and data.get("sha"):
            return data["sha"]
    except urllib.error.HTTPError:
        pass
    raise RuntimeError(f"Could not resolve {owner}/{repo}@{ref}")


def latest_semver_tag(owner: str, repo: str, token: str | None) -> str | None:
    try:
        tags = github_api(
            f"https://api.github.com/repos/{owner}/{repo}/tags?per_page=30",
            token,
        )
    except urllib.error.HTTPError:
        return None
    if not isinstance(tags, list):
        return None
    semver = re.compile(r"^v?\d+\.\d+(\.\d+)?")
    for t in tags:
        name = t.get("name") or ""
        if semver.match(name):
            return name
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pins", type=Path, default=Path("pins.yaml"))
    ap.add_argument("--out", type=Path, default=Path("pins.proposed.yaml"))
    ap.add_argument("--github-token", default=os.environ.get("GITHUB_TOKEN"))
    ap.add_argument(
        "--prefer-semver-tags",
        action="store_true",
        help="If a semver tag exists, pin to that tag tip instead of branch ref",
    )
    args = ap.parse_args()

    pins = load_pins(args.pins)
    proposed = json.loads(json.dumps(pins))  # deep copy via json
    proposed["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    proposed["notes"] = "Proposed by release/propose-pins.py — review before merge."

    decisions = []
    for name, comp in (pins.get("components") or {}).items():
        repo_url = comp.get("repository") or ""
        ref = comp.get("ref") or "devel"
        try:
            owner, repo = parse_github_repo(repo_url)
        except ValueError as e:
            decisions.append(f"{name}: skip ({e})")
            continue

        use_ref = ref
        tag = None
        if args.prefer_semver_tags:
            tag = latest_semver_tag(owner, repo, args.github_token)
            if tag:
                use_ref = tag

        try:
            sha = resolve_ref(owner, repo, use_ref, args.github_token)
        except Exception as e:
            decisions.append(f"{name}: FAILED resolve {use_ref}: {e}")
            continue

        old = (comp.get("commit") or "").strip()
        proposed["components"][name]["commit"] = sha
        if tag:
            proposed["components"][name]["ref"] = tag
        if old and old != sha:
            decisions.append(f"{name}: {old[:12]} → {sha[:12]} (via {use_ref})")
        elif not old:
            decisions.append(f"{name}: set commit {sha[:12]} (via {use_ref})")
        else:
            decisions.append(f"{name}: unchanged {sha[:12]}")

    dump_pins(proposed, args.out)
    print(f"Wrote {args.out}")
    print("Decisions:")
    for d in decisions:
        print(f"  - {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
