#!/usr/bin/env python3
"""Render release notes from pin file deltas."""
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


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def gh_repo(url: str) -> str:
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", url or "")
    if not m:
        return ""
    return f"{m.group(1)}/{m.group(2)}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prev", type=Path, required=True)
    ap.add_argument("--curr", type=Path, required=True)
    ap.add_argument("--version", required=True, help="e.g. images-v0.1.0")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    prev, curr = load(args.prev), load(args.curr)
    lines = [
        f"# {args.version}",
        "",
        f"Generated from pin delta (`{args.prev.name}` → `{args.curr.name}`).",
        "",
        "## Component pins",
        "",
        "| Component | Previous | New | Upstream |",
        "|-----------|----------|-----|----------|",
    ]

    pc = prev.get("components") or {}
    cc = curr.get("components") or {}
    all_names = sorted(set(pc) | set(cc))
    changes = 0
    for name in all_names:
        a, b = pc.get(name) or {}, cc.get(name) or {}
        old_c = (a.get("commit") or a.get("ref") or "—")
        new_c = (b.get("commit") or b.get("ref") or "—")
        if isinstance(old_c, str) and len(old_c) > 12 and re.match(r"^[0-9a-f]{40}$", old_c):
            old_s = old_c[:12]
        else:
            old_s = str(old_c)
        if isinstance(new_c, str) and len(new_c) == 40 and re.match(r"^[0-9a-f]{40}$", new_c):
            new_s = new_c[:12]
        else:
            new_s = str(new_c)
        repo = gh_repo(b.get("repository") or a.get("repository") or "")
        if old_s != new_s:
            changes += 1
            link = ""
            if repo and len(str(a.get("commit") or "")) == 40 and len(str(b.get("commit") or "")) == 40:
                link = f"[compare](https://github.com/{repo}/compare/{a.get('commit')}...{b.get('commit')})"
            elif repo:
                link = f"https://github.com/{repo}"
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | {link} |")
        else:
            lines.append(f"| {name} | `{old_s}` | `{new_s}` | (unchanged) |")

    lines += [
        "",
        f"**{changes}** component pin(s) changed.",
        "",
        "## Images to publish",
        "",
        "- `platform-ui`",
        "- `jewel-with-ui`",
        "- `awx` (only if `components.awx.build: true`)",
        "",
        "## Operator handoff",
        "",
        "1. Copy digests into `awx-platform-operator` → `release/pins.consumer.yaml`",
        "2. Bump Helm chart default image tags if needed",
        "3. Cut operator release `vX.Y.Z` after chart PR merges",
        "",
        "## Notes",
        "",
        "_Agent/human: add narrative here (why pins moved, known issues)._",
        "",
    ]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({changes} changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
