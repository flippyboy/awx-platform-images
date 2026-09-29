#!/usr/bin/env python3
"""Propose updated upstream pins for awx-platform-images.

Resolves the development branch tip (``devel``, otherwise ``main`` / ``master``)
and the registry digest of the floating development image. Does not pin stable
or semver releases — those tags are years behind where new features land.

Writes ``pins.proposed.yaml`` for an agent or human to review. The paired notes
(``release/render-notes.py --proposal``) list the upstream commits to turn into
a per-component release.
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

sys.path.insert(0, str(Path(__file__).resolve().parent))
import upstream  # noqa: E402


def load_pins(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if yaml:
        return yaml.safe_load(text)
    raise SystemExit("PyYAML required: pip install pyyaml")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pins", type=Path, default=Path("pins.yaml"))
    ap.add_argument("--out", type=Path, default=Path("pins.proposed.yaml"))
    ap.add_argument("--github-token", default=os.environ.get("GITHUB_TOKEN"))
    args = ap.parse_args()

    original = args.pins.read_text(encoding="utf-8")
    pins = load_pins(args.pins)
    updates: dict[str, dict[str, str]] = {}
    decisions: list[str] = []
    resolved = 0
    failed = 0

    for name, comp in (pins.get("components") or {}).items():
        repo_url = comp.get("repository") or ""
        configured = comp.get("ref") or "devel"
        try:
            owner, repo = upstream.parse_github_repo(repo_url)
        except ValueError as exc:
            decisions.append(f"{name}: skip ({exc})")
            failed += 1
            continue

        try:
            branch, sha = upstream.select_tracking_ref(
                owner, repo, configured, args.github_token
            )
        except Exception as exc:
            decisions.append(f"{name}: FAILED resolve development branch: {exc}")
            failed += 1
            continue

        resolved += 1
        fields: dict[str, str] = {"ref": branch, "commit": sha}
        old = (comp.get("commit") or "").strip()
        old_ref = (comp.get("ref") or "").strip()
        if upstream.is_release_tag(old_ref) or old_ref.lower() in upstream.GIT_SKIP:
            left = f"; left {old_ref} (not a development branch)"
        else:
            left = ""
        if old and (old != sha or old_ref != branch):
            decisions.append(f"{name}: {old[:12]} → {sha[:12]} via {branch}{left}")
        elif not old:
            decisions.append(f"{name}: set commit {sha[:12]} via {branch}{left}")
        else:
            decisions.append(f"{name}: unchanged {sha[:12]} via {branch}")

        public = (comp.get("public_image") or "").strip()
        if public:
            suggestion = upstream.suggest_public_image(public)
            if suggestion.get("digest"):
                fields["public_image_digest"] = suggestion["digest"]
                if suggestion.get("ignored_tag"):
                    fields["public_image"] = f"{suggestion['image']}:{suggestion['tag']}"
                    decisions.append(
                        f"{name}: ignored image tag {suggestion['ignored_tag']}; "
                        f"digest from {suggestion['tag']}"
                    )
                old_digest = (comp.get("public_image_digest") or "").strip()
                short = suggestion["digest"][:19]
                if old_digest != suggestion["digest"]:
                    decisions.append(
                        f"{name}: image {suggestion['image']}:{suggestion['tag']}@{short}…"
                    )
                else:
                    decisions.append(f"{name}: image digest unchanged {short}…")
            else:
                decisions.append(
                    f"{name}: image digest FAILED ({suggestion.get('error')})"
                )
        updates[name] = fields

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        text, changed = upstream.apply_pin_updates(original, updates, updated=stamp)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    args.out.write_text(text, encoding="utf-8")
    print(f"Wrote {args.out} ({'changes' if changed else 'no pin changes'})")
    print("Decisions:")
    for line in decisions:
        print(f"  - {line}")
    if resolved == 0 and failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
