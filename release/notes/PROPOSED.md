# Proposed pin update

Proposal for the next **pinned** image release. Upstream stable and semver
tags are not candidates — those releases lag the branches where new features
land (`devel`, or `main` when that is the development branch).

Each git pin is that branch's tip commit. Each public image pin is the
registry digest of the floating development tag (`devel` / `latest`), not a
stable version tag.

**Review before merge.** This is the input for cutting a release, not the release.

Generated from pin delta (`pins.prev.yaml` → `pins.proposed.yaml`).

## Upstream pins

| Upstream | Previous | Proposed | Link |
|----------|----------|----------|------|
| awx | `8565291e43e1 via devel` | `8565291e43e1 via devel` | (unchanged) |
| jewel | `d45bfa998811 via devel` | `a39b016d5bc6 via devel` | [compare](https://github.com/ansible/jewel/compare/d45bfa9988112739d48ce2e7fda08e0d9d12104a...a39b016d5bc6846a4d6262d4820dbcc91daf355a) |
| ansible-ui | `e7017aada0ba via devel` | `8b64849d386e via devel` | [compare](https://github.com/ansible/ansible-ui/compare/e7017aada0ba1334f70699aea58012dcfe4fe60a...8b64849d386e41bfbe1c3ce4d7d2722092cc1039) |

**2** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

Unchanged at `8565291e43e1`.

### `jewel` (`devel`)

`d45bfa998811` → `a39b016d5bc6` — 3 commits. [compare](https://github.com/ansible/jewel/compare/d45bfa9988112739d48ce2e7fda08e0d9d12104a...a39b016d5bc6846a4d6262d4820dbcc91daf355a)

- [`722defcd6269`](https://github.com/ansible/jewel/commit/722defcd626905370aa7eccfc48eca93512dc9d6) 2026-10-30 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to d29f036 (#320)
- [`1aa46a8bd6bf`](https://github.com/ansible/jewel/commit/1aa46a8bd6bf35c2ee078d0e2a9b98cafd47bfeb) 2026-10-30 [AAP-98757]: Harden migration upgrade CI checks (#303)
- [`a39b016d5bc6`](https://github.com/ansible/jewel/commit/a39b016d5bc6846a4d6262d4820dbcc91daf355a) 2026-10-30 AAP-100207 Remove condition for prepping request.POST in control_plane (#317)

### `ansible-ui` (`devel`)

`e7017aada0ba` → `8b64849d386e` — 1 commits. [compare](https://github.com/ansible/ansible-ui/compare/e7017aada0ba1334f70699aea58012dcfe4fe60a...8b64849d386e41bfbe1c3ce4d7d2722092cc1039)

- [`8b64849d386e`](https://github.com/ansible/ansible-ui/commit/8b64849d386e41bfbe1c3ce4d7d2722092cc1039) 2026-10-30 AAP-95527 XLAB Address low priority Automation Dashboard review comments (#3841)

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:db7b4c9b3bd225e6d28c4b210f15c3d4d7799ffb0ab55dc352b5b0b46724a8ab` | `ghcr.io/ansible/awx:devel@sha256:db7b4c9b3bd225e6d28c4b210f15c3d4d7799ffb0ab55dc352b5b0b46724a8ab` | (unchanged) |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | (unchanged) |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake).

Image versions are calver `YYYY.MM.DD` (zero-padded month and day, UTC).
Another cut the same day uses `YYYY.MM.DD-N`, and N starts at 1.

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v2026.11.02` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v2026.11.02` | upstream moved: `jewel` |
| `awx` | — | skipped (`components.awx.build` is false) |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Set `published.<component>.version` to the UTC calver only for tracks
   whose triggers moved. The first cut that day is `YYYY.MM.DD`. A later
   cut the same day is `2026.11.02-1`, `2026.11.02-2`, and so on.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.11.02 \
  --out release/notes/platform-ui-v2026.11.02.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component image is published, `release-images` dispatches
`images-released`. The operator repo pins that tag and digest and cuts
`vYYYY.MM.DD`. Do not open a second pin pull request for the same image.
See `release/AGENTS.md` and `docs/awx-image.md`.

