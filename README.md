# awx-platform-images

Build pipelines and compose testing for modern AWX **component images**.

This repository **does not fork** application source trees. CI checks out:

| Component | Upstream (untouched) |
|-----------|----------------------|
| Controller | [ansible/awx](https://github.com/ansible/awx) |
| Jewel | [ansible/jewel](https://github.com/ansible/jewel) |
| Platform UI | [ansible/ansible-ui](https://github.com/ansible/ansible-ui) |

…at pins defined in [`pins.yaml`](./pins.yaml), then builds with **this repo’s Dockerfiles**
(and optional build-time patches, e.g. open-license UI banner).

Companion product repo: **[awx-platform-operator](https://github.com/flippyboy/awx-platform-operator)**  
(operator + Helm + CRDs).

## Images published (GHCR)

All packages under `ghcr.io/flippyboy/awx/…` (shared namespace with the operator repo).
**Each image has its own release train** (independent git tags and versions):

| Image | Git tag | Description |
|-------|---------|-------------|
| `ghcr.io/flippyboy/awx/platform-ui:X.Y.Z` | `platform-ui-vX.Y.Z` | ansible-ui `platform/` workspace + patches |
| `ghcr.io/flippyboy/awx/jewel-with-ui:X.Y.Z` | `jewel-with-ui-vX.Y.Z` | Jewel base + baked Platform UI |
| `ghcr.io/ansible/awx` | — | Default Controller (optional rebuild: `awx-v*` → `ghcr.io/flippyboy/awx/awx`) |

`jewel-with-ui` pulls a **published** `platform-ui` tag at build time (does not rebuild UI in the same release).

## Layout

```text
pins.yaml                 # source of truth for upstream git refs
docker/                   # Dockerfiles + UI patches
compose/                  # docker-compose for local stack testing
config/                   # compose settings (awx, jewel, …)
scripts/                  # bootstrap, entrypoints
release/                  # agent-assisted pin/release tooling
  AGENTS.md               # instructions for coding agents
  propose-pins.py         # fetch upstream tags / commits
  render-notes.py         # generate release notes from pin deltas
  cadence.yaml            # steady-cadence policy
docs/
.github/workflows/
```

## Local compose (testing)

```bash
# Optionally set pins and build
cp .env.example .env   # if present
make build             # platform-ui + jewel-with-ui
make up
make trust             # JWT Jewel ↔ Controller
# UI: https://localhost
```

Upstream git checkouts for **source** builds (optional):

```bash
./scripts/fetch-upstream.sh   # clones ansible/* at pins into .upstream/
```

## Agent-assisted / per-component releases

See [`release/AGENTS.md`](./release/AGENTS.md). Short version:

```bash
# Propose new upstream pins
python release/propose-pins.py --pins pins.yaml --out pins.proposed.yaml

# After merging pin changes that affect UI only:
python release/render-notes.py \
  --prev pins.prev.yaml --curr pins.yaml \
  --component platform-ui --version 0.1.1 \
  --out release/notes/platform-ui-v0.1.1.md
git tag platform-ui-v0.1.1 && git push origin platform-ui-v0.1.1

# Later, rebake jewel with that UI (or after jewel pin moves):
python release/render-notes.py \
  --prev pins.prev.yaml --curr pins.yaml \
  --component jewel-with-ui --version 0.1.1 \
  --platform-ui-version 0.1.1 \
  --out release/notes/jewel-with-ui-v0.1.1.md
git tag jewel-with-ui-v0.1.1 && git push origin jewel-with-ui-v0.1.1
```

Or use **Actions → release-images → Run workflow** (component + version).

Steady cadence is defined in `release/cadence.yaml` (e.g. weekly pin bump PR).

## Relationship to operator repo

| Repo | Releases |
|------|----------|
| **images** | Per-component tags (`platform-ui-v…`, `jewel-with-ui-v…`) |
| **operator** | `v0.1.0` — operator image + Helm; pins only the component versions it needs |
