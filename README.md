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

| Image | Description |
|-------|-------------|
| `platform-ui` | ansible-ui `platform/` workspace + patches |
| `jewel-with-ui` | Jewel base + baked Platform UI |
| `awx` | Optional rebuild of Controller (or skip and use public `ghcr.io/ansible/awx`) |

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

## Agent-assisted releases

See [`release/AGENTS.md`](./release/AGENTS.md). Short version:

```bash
# Propose new pins (reads GitHub tags / default branches)
python release/propose-pins.py --write pins.proposed.yaml

# Agent (or human) reviews pins.proposed.yaml → merges into pins.yaml
# Then generate notes + tag
python release/render-notes.py --prev pins.prev.yaml --curr pins.yaml -o release/notes/images-v0.1.0.md
```

Steady cadence is defined in `release/cadence.yaml` (e.g. weekly pin bump PR).

## Relationship to operator repo

| Repo | Releases |
|------|----------|
| **images** | `images-v0.1.0` — component image digests |
| **operator** | `v0.1.0` — operator image + Helm chart consuming those digests |
