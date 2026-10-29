#!/usr/bin/env bash
# Prepare the docker build context for the Jewel base image: check out
# ansible/jewel at the pin and render its Containerfile with upstream's own
# generator (make tools/generated/sources).
#
# Upstream publishes ghcr.io/ansible/jewel:latest only when its own image
# workflow succeeds, so that tag can lag the source by days. Building from the
# pinned commit ships the dependency fixes that already landed upstream.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
CTX="${BUILD_CONTEXT:-$ROOT/.build/jewel-context}"
TOOLS="${JEWEL_TOOLS_VENV:-$ROOT/.build/jewel-tools}"
# Same ansible-core release upstream's build-image workflow renders with.
ANSIBLE_CORE_VERSION="${ANSIBLE_CORE_VERSION:-2.21.1}"
rm -rf "$CTX"
mkdir -p "$(dirname "$CTX")"

python3 - "$ROOT/pins.yaml" "$CTX" <<'PY'
import sys, subprocess, pathlib

pins_path, dest = map(pathlib.Path, sys.argv[1:3])
import yaml

pins = yaml.safe_load(pins_path.read_text())
jewel = pins["components"]["jewel"]
repo = jewel["repository"]
ref_branch = jewel.get("ref") or "devel"
commit = (jewel.get("commit") or "").strip()
print(f">> clone {repo} @ branch={ref_branch} commit={commit or '-'}")
subprocess.check_call(
    ["git", "clone", "--depth", "1", "--branch", ref_branch, repo, str(dest)]
)
if commit:
    subprocess.check_call(
        ["git", "-C", str(dest), "fetch", "--depth", "1", "origin", commit]
    )
    subprocess.check_call(["git", "-C", str(dest), "checkout", commit])
PY

if [[ ! -x "$TOOLS/bin/ansible-playbook" ]]; then
  python3 -m venv "$TOOLS"
  "$TOOLS/bin/pip" install --quiet --only-binary :all: "ansible-core==${ANSIBLE_CORE_VERSION}"
fi
PATH="$TOOLS/bin:$PATH" make -C "$CTX" tools/generated/sources >/dev/null
test -f "$CTX/tools/generated/Containerfile"
echo ">> context ready $CTX"

echo "Build with:"
echo "  docker build -f $CTX/tools/generated/Containerfile --target jewel -t jewel-base:local $CTX"
