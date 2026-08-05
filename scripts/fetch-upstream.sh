#!/usr/bin/env bash
# Shallow-clone upstream component repos at pins.yaml refs into .upstream/
# Does not modify upstream trees; for local source builds only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PINS="${PINS:-pins.yaml}"
OUT="${UPSTREAM_DIR:-$ROOT/.upstream}"
mkdir -p "$OUT"

if ! command -v python3 >/dev/null; then
  echo "python3 required" >&2
  exit 1
fi

python3 - <<'PY' "$PINS" "$OUT"
import sys, subprocess, pathlib
pins_path, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
try:
    import yaml
except ImportError:
    raise SystemExit("pip install pyyaml")
pins = yaml.safe_load(pins_path.read_text())
for name, c in (pins.get("components") or {}).items():
    repo = c.get("repository")
    ref = c.get("commit") or c.get("ref") or "devel"
    dest = out / name
    print(f">> {name}: {repo} @ {ref}")
    if dest.exists():
        subprocess.check_call(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref], cwd=dest)
        subprocess.check_call(["git", "-C", str(dest), "checkout", "FETCH_HEAD"])
    else:
        subprocess.check_call([
            "git", "clone", "--depth", "1", "--branch", c.get("ref") or "devel",
            repo, str(dest),
        ])
        if c.get("commit"):
            subprocess.check_call(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", c["commit"]])
            subprocess.check_call(["git", "-C", str(dest), "checkout", c["commit"]])
print(">> done", out)
PY
