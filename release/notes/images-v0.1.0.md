# awx-platform-images images-v0.1.0

Initial scaffold of **component image build pipelines** and compose testing for modern AWX.

## Philosophy

- **No forks** of [ansible/awx](https://github.com/ansible/awx), [ansible/jewel](https://github.com/ansible/jewel), or [ansible/ansible-ui](https://github.com/ansible/ansible-ui).
- Builds check out upstream at pins in `pins.yaml` (commit SHAs preferred for releases).
- Build-time Dockerfiles and UI patches live only in this repository.

## Images (target GHCR)

| Image | Description |
|-------|-------------|
| `ghcr.io/flippyboy/awx/platform-ui` | Platform UI from ansible-ui + open-license patches |
| `ghcr.io/flippyboy/awx/jewel-with-ui` | Jewel + baked Platform UI |
| `ghcr.io/ansible/awx` (public) | Default Controller image; optional rebuild later |

## Tooling

- `pins.yaml` — source of truth for upstream refs
- `release/propose-pins.py` — agent/human pin proposals (GitHub API)
- `release/render-notes.py` — pin-delta release notes
- `release/cadence.yaml` + weekly `propose-pins` workflow
- Compose stack under `compose/` for local integration testing

## Companion

Operator + Helm releases: [awx-platform-operator](https://github.com/flippyboy/awx-platform-operator).

## Initial pins (scaffold)

See `pins.yaml`. Run `python release/propose-pins.py` to resolve current SHAs before the next cadence cut.
