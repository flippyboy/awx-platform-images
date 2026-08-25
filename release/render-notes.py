#!/usr/bin/env python3
"""Render pin-delta notes: per-component releases, or a weekly proposal."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# Which upstream pins matter for each publishable image
COMPONENT_UPSTREAM: dict[str, list[str]] = {
    "platform-ui": ["ansible-ui"],
    "jewel-with-ui": ["jewel", "ansible-ui"],
    "awx": ["awx"],
}


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def gh_repo(url: str) -> str:
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", url or "")
    if not m:
        return ""
    return f"{m.group(1)}/{m.group(2)}"


def short_ref(val: object) -> str:
    s = str(val or "—")
    if len(s) == 40 and re.match(r"^[0-9a-f]{40}$", s):
        return s[:12]
    return s


def pin_changed(old: dict, new: dict) -> bool:
    return (old.get("commit") or "") != (new.get("commit") or "") or (
        old.get("ref") or ""
    ) != (new.get("ref") or "")


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
        return (
            f"[compare](https://github.com/{repo}/compare/{old_c}...{new_c})"
        )
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
        if pin_changed(old, new):
            changes += 1
            link = compare_link(old, new)
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | {link} |")
        else:
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | (unchanged) |")
    return lines, changes


def relevant_upstreams(component: str, curr: dict) -> list[str]:
    relevant = list(COMPONENT_UPSTREAM[component])
    derived = (curr.get("derived") or {}).get(component) or {}
    if derived.get("release_triggers"):
        relevant = list(derived["release_triggers"])
    return relevant


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
            or ((curr.get("published") or {}).get("platform-ui") or {}).get(
                "version"
            )
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
        "_Agent/human: add narrative here (why this component moved, known issues)._",
        "",
    ]
    return lines, changes


def render_proposal(
    *, prev: dict, curr: dict, prev_name: str, curr_name: str
) -> tuple[list[str], int]:
    pc = prev.get("components") or {}
    cc = curr.get("components") or {}
    names = sorted(set(pc) | set(cc))

    lines = [
        "# Proposed pin update",
        "",
        "Automated weekly proposal. **Review before merge.** This is not a release.",
        "",
        f"Generated from pin delta (`{prev_name}` → `{curr_name}`).",
        "",
        "## Upstream pins",
        "",
        "| Upstream | Previous | New | Link |",
        "|----------|----------|-----|------|",
    ]
    rows, changes = pin_table_rows(names, pc, cc)
    lines += rows
    lines += [
        "",
        f"**{changes}** upstream pin(s) changed.",
        "",
        "## Image tracks to consider",
        "",
        "Cut a component tag only after review. Independent trains:",
        "",
        "| Track | Git tag | Why |",
        "|-------|---------|-----|",
    ]

    derived = curr.get("derived") or {}
    for track in ("platform-ui", "jewel-with-ui", "awx"):
        spec = derived.get(track) or {}
        triggers = list(
            spec.get("release_triggers")
            or COMPONENT_UPSTREAM.get(track)
            or []
        )
        moved = [t for t in triggers if pin_changed(pc.get(t) or {}, cc.get(t) or {})]
        if track == "awx" and not (cc.get("awx") or {}).get("build"):
            reason = "skipped (`components.awx.build` is false)"
        elif moved:
            reason = "upstream moved: " + ", ".join(f"`{t}`" for t in moved)
        else:
            reason = "no trigger pin changed"
        lines.append(f"| `{track}` | `{track}-vX.Y.Z` | {reason} |")

    lines += [
        "",
        "## Operator handoff",
        "",
        "After a component is actually released:",
        "",
        "1. Bump **only** that image in `awx-platform-operator` → `release/pins.consumer.yaml`.",
        "2. Leave other component pins unchanged.",
        "3. See `release/AGENTS.md`.",
        "",
        "## Notes",
        "",
        "_Agent/human: accept, hold, or revert individual pins before merge._",
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
        lines, changes = render_proposal(
            prev=prev,
            curr=curr,
            prev_name=args.prev.name,
            curr_name=args.curr.name,
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
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({changes} pin changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
