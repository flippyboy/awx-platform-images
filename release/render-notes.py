#!/usr/bin/env python3
"""Render pin-delta notes: per-component releases, or a weekly proposal.

Proposals are the review input for a pinned release. They list development-branch
commits since the current pin (the changelog) and the floating image digest.
Stable upstream tags are not release candidates.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import upstream  # noqa: E402

# Which upstream pins matter for each publishable image
COMPONENT_UPSTREAM: dict[str, list[str]] = {
    "platform-ui": ["ansible-ui"],
    "jewel-with-ui": ["jewel", "ansible-ui"],
    "awx": ["awx"],
}


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def gh_repo(url: str) -> str:
    try:
        owner, repo = upstream.parse_github_repo(url)
    except ValueError:
        return ""
    return f"{owner}/{repo}"


def short_ref(val: object) -> str:
    s = str(val or "—")
    if len(s) == 40 and re.match(r"^[0-9a-f]{40}$", s):
        return s[:12]
    return s


def format_pin(comp: dict) -> str:
    commit = (comp.get("commit") or "").strip()
    ref = (comp.get("ref") or "").strip()
    if commit:
        shown = short_ref(commit)
        return f"{shown} via {ref}" if ref else shown
    return ref or "—"


def compare_link(old: dict, new: dict) -> str:
    repo = gh_repo(new.get("repository") or old.get("repository") or "")
    old_c, new_c = str(old.get("commit") or ""), str(new.get("commit") or "")
    if repo and len(old_c) == 40 and len(new_c) == 40:
        return f"[compare](https://github.com/{repo}/compare/{old_c}...{new_c})"
    if repo:
        return f"https://github.com/{repo}"
    return ""


def pin_table_rows(
    names: list[str], prev_comps: dict, curr_comps: dict
) -> tuple[list[str], int]:
    lines: list[str] = []
    changes = 0
    for name in names:
        old, new = prev_comps.get(name) or {}, curr_comps.get(name) or {}
        if not old and not new:
            lines.append(f"| {name} | — | — | (not in pins) |")
            continue
        old_s, new_s = format_pin(old), format_pin(new)
        moved = upstream.git_changed(old, new) or upstream.image_changed(old, new)
        if moved:
            changes += 1
            link = compare_link(old, new)
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | {link} |")
        else:
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | (unchanged) |")
    return lines, changes


def image_table_rows(names: list[str], prev_comps: dict, curr_comps: dict) -> list[str]:
    lines: list[str] = []
    for name in names:
        old, new = prev_comps.get(name) or {}, curr_comps.get(name) or {}
        if not (old.get("public_image") or new.get("public_image")):
            continue
        old_ref = upstream.pinned_image_ref(
            old.get("public_image") or "", old.get("public_image_digest")
        )
        new_ref = upstream.pinned_image_ref(
            new.get("public_image") or "", new.get("public_image_digest")
        )
        if not new.get("public_image_digest"):
            new_ref = new_ref or "—"
            note = "digest not resolved"
        elif upstream.image_changed(old, new):
            note = "development tag; stable versions are not used"
        else:
            note = "(unchanged)"
        lines.append(f"| `{name}` | `{old_ref or '—'}` | `{new_ref}` | {note} |")
    return lines


def relevant_upstreams(component: str, curr: dict) -> list[str]:
    relevant = list(COMPONENT_UPSTREAM[component])
    derived = (curr.get("derived") or {}).get(component) or {}
    if derived.get("release_triggers"):
        relevant = list(derived["release_triggers"])
    return relevant


def next_patch(version: str) -> str:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", (version or "").strip())
    if not match:
        return "X.Y.Z"
    return f"{match.group(1)}.{match.group(2)}.{int(match.group(3)) + 1}"


def collect_commit_logs(
    prev: dict, curr: dict, names: list[str], token: str | None
) -> dict[str, dict]:
    logs: dict[str, dict] = {}
    prev_c = prev.get("components") or {}
    curr_c = curr.get("components") or {}
    for name in names:
        old, new = prev_c.get(name) or {}, curr_c.get(name) or {}
        if not upstream.git_changed(old, new):
            logs[name] = {"skipped": True}
            continue
        repo_url = new.get("repository") or old.get("repository") or ""
        try:
            owner, repo = upstream.parse_github_repo(repo_url)
        except ValueError as exc:
            logs[name] = {
                "error": str(exc),
                "commits": [],
                "truncated": False,
                "reached_base": False,
            }
            continue
        head = (new.get("commit") or new.get("ref") or "devel").strip()
        base = (old.get("commit") or "").strip()
        try:
            logs[name] = upstream.commits_since(owner, repo, base, head, token)
        except Exception as exc:
            logs[name] = {
                "error": str(exc),
                "commits": [],
                "truncated": False,
                "reached_base": False,
            }
    return logs


def commit_sections(
    names: list[str], prev: dict, curr: dict, logs: dict[str, dict]
) -> list[str]:
    prev_c = prev.get("components") or {}
    curr_c = curr.get("components") or {}
    lines: list[str] = []
    for name in names:
        old, new = prev_c.get(name) or {}, curr_c.get(name) or {}
        if not old and not new:
            continue
        if not upstream.git_changed(old, new):
            info = {"skipped": True}
        else:
            info = logs.get(name) or {
                "error": "commit list not fetched",
                "commits": [],
                "truncated": False,
                "reached_base": False,
            }
        block = upstream.format_commit_log(
            name,
            (new.get("ref") or old.get("ref") or "devel"),
            str(old.get("commit") or ""),
            str(new.get("commit") or ""),
            info,
            gh_repo(new.get("repository") or old.get("repository") or ""),
        )
        old_ref = str(old.get("ref") or "")
        if upstream.is_release_tag(old_ref) or old_ref.lower() in upstream.GIT_SKIP:
            note = (
                f"Ignored previous ref `{old_ref}` — stable tags and floating names "
                "are not the development branch."
            )
            block = block[:2] + [note, ""] + block[2:]
        lines += block
    return lines


def render_release(
    *,
    prev: dict,
    curr: dict,
    component: str,
    version: str,
    platform_ui_version: str,
    registry_prefix: str,
    prev_name: str,
    curr_name: str,
    commit_logs: dict[str, dict],
) -> tuple[list[str], int]:
    prefix = (curr.get("registry") or {}).get("prefix") or registry_prefix
    image = f"{prefix}/{component}:{version}"
    git_tag = f"{component}-v{version}"
    relevant = relevant_upstreams(component, curr)

    lines = [
        f"# {component} {version}",
        "",
        f"Independent component release. Git tag: `{git_tag}`.",
        "",
        f"Generated from pin delta (`{prev_name}` → `{curr_name}`).",
        "",
        "## Image",
        "",
        f"`{image}`",
        "",
    ]

    if component == "jewel-with-ui":
        pui = platform_ui_version.lstrip("v") or (
            ((curr.get("published") or {}).get("jewel-with-ui") or {}).get(
                "platform_ui_version"
            )
            or ((curr.get("published") or {}).get("platform-ui") or {}).get("version")
            or "?"
        )
        lines += [
            "## Baked platform-ui",
            "",
            f"`{prefix}/platform-ui:{pui}`",
            "",
            "This release does **not** rebuild platform-ui; it pulls the published UI image above.",
            "",
        ]
        jewel = (curr.get("components") or {}).get("jewel") or {}
        if jewel.get("public_image") or jewel.get("public_image_digest"):
            base = upstream.pinned_image_ref(
                jewel.get("public_image") or "", jewel.get("public_image_digest")
            )
            lines += [
                "## Jewel base image",
                "",
                f"`{base}`",
                "",
                "Development image (`latest` / `devel`). A pinned digest is what the "
                "release build pulls. Stable upstream version tags are not used.",
                "",
            ]

    lines += [
        "## Upstream pins (relevant)",
        "",
        "| Upstream | Previous | New | Link |",
        "|----------|----------|-----|------|",
    ]
    rows, changes = pin_table_rows(
        relevant, prev.get("components") or {}, curr.get("components") or {}
    )
    lines += rows
    lines += [
        "",
        f"**{changes}** relevant upstream pin(s) changed.",
        "",
        "## Upstream commits",
        "",
        "Changes on the development branch since the previous pin. "
        "This is the changelog for the release.",
        "",
    ]
    lines += commit_sections(relevant, prev, curr, commit_logs)
    lines += [
        "## Operator handoff",
        "",
        f"1. Bump **only** `{component}` in `awx-platform-operator` → `release/pins.consumer.yaml`",
        f"   (tag `{version}` + digest once available).",
        "2. Update Helm chart default image tag for this component if it is a chart default.",
        "3. Leave other component pins unchanged — they have independent release trains.",
        "4. Cut an operator release only when the operator itself or chart defaults need a ship.",
        "",
        "## Notes",
        "",
        "_Agent/human: add a short narrative (why this cut, known issues). "
        "The commit list above is the upstream changelog._",
        "",
    ]
    return lines, changes


def render_proposal(
    *,
    prev: dict,
    curr: dict,
    prev_name: str,
    curr_name: str,
    commit_logs: dict[str, dict],
) -> tuple[list[str], int]:
    pc = prev.get("components") or {}
    cc = curr.get("components") or {}
    names = list(dict.fromkeys(list(pc) + list(cc)))

    lines = [
        "# Proposed pin update",
        "",
        "Proposal for the next **pinned** image release. Upstream stable and semver",
        "tags are not candidates — those releases lag the branches where new features",
        "land (`devel`, or `main` when that is the development branch).",
        "",
        "Each git pin is that branch's tip commit. Each public image pin is the",
        "registry digest of the floating development tag (`devel` / `latest`), not a",
        "stable version tag.",
        "",
        "**Review before merge.** This is the input for cutting a release, not the release.",
        "",
        f"Generated from pin delta (`{prev_name}` → `{curr_name}`).",
        "",
        "## Upstream pins",
        "",
        "| Upstream | Previous | Proposed | Link |",
        "|----------|----------|----------|------|",
    ]
    rows, changes = pin_table_rows(names, pc, cc)
    lines += rows
    lines += [
        "",
        f"**{changes}** upstream pin(s) changed.",
        "",
        "## Upstream commits",
        "",
        "Use this list as the release-note changelog when you cut a component.",
        "Subjects are the upstream commit messages.",
        "",
    ]
    lines += commit_sections(names, prev, curr, commit_logs)

    image_rows = image_table_rows(names, pc, cc)
    if image_rows:
        lines += [
            "## Public image digests",
            "",
            "Resolved from the development tag. Stable version tags are ignored.",
            "",
            "| Component | Previous | Proposed | Note |",
            "|-----------|----------|----------|------|",
        ]
        lines += image_rows
        lines.append("")

    lines += [
        "## Image tracks to consider",
        "",
        "Cut a component tag only after review. Independent trains",
        "(prefer one component per release unless you mean to rebake):",
        "",
        "| Track | Suggested tag | Why |",
        "|-------|---------------|-----|",
    ]

    published = curr.get("published") or {}
    derived = curr.get("derived") or {}
    for track in ("platform-ui", "jewel-with-ui", "awx"):
        spec = derived.get(track) or {}
        triggers = list(spec.get("release_triggers") or COMPONENT_UPSTREAM.get(track) or [])
        moved = [
            t
            for t in triggers
            if upstream.git_changed(pc.get(t) or {}, cc.get(t) or {})
            or upstream.image_changed(pc.get(t) or {}, cc.get(t) or {})
        ]
        current = str((published.get(track) or {}).get("version") or "")
        if track == "awx" and not (cc.get("awx") or {}).get("build"):
            if moved:
                reason = (
                    "upstream moved, but `components.awx.build` is false — "
                    "record the digest, do not cut an awx image"
                )
            else:
                reason = "skipped (`components.awx.build` is false)"
            tag = "—"
        elif moved:
            version = next_patch(current)
            tag = f"`{track}-v{version}`"
            reason = "upstream moved: " + ", ".join(f"`{t}`" for t in moved)
        else:
            tag = f"keep `{current}`" if current else "—"
            reason = "no trigger pin changed"
        lines.append(f"| `{track}` | {tag} | {reason} |")

    lines += [
        "",
        "## Agent next step",
        "",
        "1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.",
        "2. Keep `ref` on the development branch. `commit` is that branch's tip.",
        "   `public_image_digest` is the matching image digest — do not substitute a",
        "   stable version tag.",
        "3. Bump `published.<component>.version` only for tracks whose triggers moved.",
        "4. Render that component's notes (they include this commit list) and add a",
        "   short narrative at the bottom:",
        "",
        "```bash",
        "python release/render-notes.py \\",
        "  --prev pins.prev.yaml \\",
        "  --curr pins.yaml \\",
        "  --component platform-ui \\",
        "  --version X.Y.Z \\",
        "  --out release/notes/platform-ui-vX.Y.Z.md",
        "```",
        "",
        "5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.",
        "",
        "## Operator handoff",
        "",
        "After a component is actually released:",
        "",
        "1. Bump **only** that image in `awx-platform-operator` → `release/pins.consumer.yaml`.",
        "2. Leave other component pins unchanged.",
        "3. See `release/AGENTS.md`.",
        "",
    ]
    return lines, changes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prev", type=Path, required=True)
    ap.add_argument("--curr", type=Path, required=True)
    ap.add_argument(
        "--proposal",
        action="store_true",
        help="Combined pin-proposal notes (weekly workflow). Do not use for a release.",
    )
    ap.add_argument(
        "--component",
        choices=sorted(COMPONENT_UPSTREAM),
        help="Publishable image being released (required unless --proposal)",
    )
    ap.add_argument(
        "--version",
        help="Semver for this component, e.g. 0.1.1 (required unless --proposal)",
    )
    ap.add_argument(
        "--platform-ui-version",
        default="",
        help="For jewel-with-ui: platform-ui image tag baked into this release",
    )
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument(
        "--registry-prefix",
        default="ghcr.io/flippyboy/awx",
        help="GHCR prefix for the image line",
    )
    ap.add_argument(
        "--github-token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub token for upstream commit messages (public repos work without one)",
    )
    ap.add_argument(
        "--offline",
        action="store_true",
        help="Do not call GitHub. Commit sections will say the list was not fetched.",
    )
    args = ap.parse_args()

    if args.proposal:
        if args.component or args.version:
            ap.error("--proposal cannot be combined with --component/--version")
    else:
        if not args.component:
            ap.error("--component is required unless --proposal is set")
        if not args.version:
            ap.error("--version is required unless --proposal is set")

    prev, curr = load(args.prev), load(args.curr)
    if args.proposal:
        names = list(
            dict.fromkeys(
                list((prev.get("components") or {})) + list((curr.get("components") or {}))
            )
        )
    else:
        names = relevant_upstreams(args.component, curr)

    if args.offline:
        logs = {name: {"error": "offline; commit list not fetched"} for name in names}
    else:
        logs = collect_commit_logs(prev, curr, names, args.github_token)

    if args.proposal:
        lines, changes = render_proposal(
            prev=prev,
            curr=curr,
            prev_name=args.prev.name,
            curr_name=args.curr.name,
            commit_logs=logs,
        )
    else:
        lines, changes = render_release(
            prev=prev,
            curr=curr,
            component=args.component,
            version=args.version.lstrip("v"),
            platform_ui_version=args.platform_ui_version,
            registry_prefix=args.registry_prefix,
            prev_name=args.prev.name,
            curr_name=args.curr.name,
            commit_logs=logs,
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({changes} pin changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
