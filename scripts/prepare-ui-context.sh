#!/usr/bin/env bash
# Prepare docker build context for platform-ui: checkout ansible-ui at pin.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
CTX="${BUILD_CONTEXT:-$ROOT/.build/ui-context}"
rm -rf "$CTX"
mkdir -p "$CTX"

python3 - "$ROOT/pins.yaml" "$CTX" "$ROOT" <<'PY'
import sys, subprocess, pathlib, shutil

pins_path, ctx, root = map(pathlib.Path, sys.argv[1:4])
import yaml

pins = yaml.safe_load(pins_path.read_text())
ui = pins["components"]["ansible-ui"]
repo = ui["repository"]
ref_branch = ui.get("ref") or "devel"
commit = (ui.get("commit") or "").strip()
dest = ctx / "ansible-ui"
print(f">> clone {repo} @ branch={ref_branch} commit={commit or '-'}")
subprocess.check_call(
    ["git", "clone", "--depth", "1", "--branch", ref_branch, repo, str(dest)]
)
if commit:
    subprocess.check_call(
        ["git", "-C", str(dest), "fetch", "--depth", "1", "origin", commit]
    )
    subprocess.check_call(["git", "-C", str(dest), "checkout", commit])
shutil.copytree(
    root / "docker" / "platform-ui",
    ctx / "docker" / "platform-ui",
    dirs_exist_ok=True,
)
print(">> context ready", ctx)
PY

echo "Build with:"
echo "  docker build -f $CTX/docker/platform-ui/Dockerfile -t platform-ui:local $CTX"
