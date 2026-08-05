#!/usr/bin/env python3
"""Render per-component release notes from pin file deltas."""
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prev", type=Path, required=True)
    ap.add_argument("--curr", type=Path, required=True)
    ap.add_argument(
        "--component",
        required=True,
        choices=sorted(COMPONENT_UPSTREAM),
        help="Publishable image being released",
    )
    ap.add_argument(
        "--version",
        required=True,
        help="Semver for this component, e.g. 0.1.1 (notes title uses <component> <version>)",
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

    version = args.version.lstrip("v")
    component = args.component
    prev, curr = load(args.prev), load(args.curr)
    prefix = (
        (curr.get("registry") or {}).get("prefix")
        or args.registry_prefix
    )
    image = f"{prefix}/{component}:{version}"
    git_tag = f"{component}-v{version}"

    relevant = COMPONENT_UPSTREAM[component]
    # Prefer derived.release_triggers when present
    derived = (curr.get("derived") or {}).get(component) or {}
    if derived.get("release_triggers"):
        relevant = list(derived["release_triggers"])
        # still show ansible-ui for jewel notes if platform-ui-version set
        if component == "jewel-with-ui" and "ansible-ui" not in relevant:
            pass

    lines = [
        f"# {component} {version}",
        "",
        f"Independent component release. Git tag: `{git_tag}`.",
        "",
        f"Generated from pin delta (`{args.prev.name}` → `{args.curr.name}`).",
        "",
        "## Image",
        "",
        f"`{image}`",
        "",
    ]

    if component == "jewel-with-ui":
        pui = args.platform_ui_version.lstrip("v") or (
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

    lines += [
        "## Upstream pins (relevant)",
        "",
        "| Upstream | Previous | New | Link |",
        "|----------|----------|-----|------|",
    ]

    pc = prev.get("components") or {}
    cc = curr.get("components") or {}
    changes = 0
    for name in relevant:
        a, b = pc.get(name) or {}, cc.get(name) or {}
        if not a and not b:
            lines.append(f"| {name} | — | — | (not in pins) |")
            continue
        old_c = a.get("commit") or a.get("ref") or "—"
        new_c = b.get("commit") or b.get("ref") or "—"
        old_s, new_s = short_ref(old_c), short_ref(new_c)
        repo = gh_repo(b.get("repository") or a.get("repository") or "")
        if old_s != new_s:
            changes += 1
            link = ""
            if (
                repo
                and len(str(a.get("commit") or "")) == 40
                and len(str(b.get("commit") or "")) == 40
            ):
                link = (
                    f"[compare](https://github.com/{repo}/compare/"
                    f"{a.get('commit')}...{b.get('commit')})"
                )
            elif repo:
                link = f"https://github.com/{repo}"
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | {link} |")
        else:
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | (unchanged) |")

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

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({changes} relevant pin changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
