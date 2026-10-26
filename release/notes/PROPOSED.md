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
| awx | `edabe5d6eb7d via devel` | `edabe5d6eb7d via devel` | (unchanged) |
| jewel | `f664db1b715e via devel` | `f664db1b715e via devel` | (unchanged) |
| ansible-ui | `48e8281db67d via devel` | `48e8281db67d via devel` | (unchanged) |

**0** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

Unchanged at `edabe5d6eb7d`.

### `jewel` (`devel`)

Unchanged at `f664db1b715e`.

### `ansible-ui` (`devel`)

Unchanged at `48e8281db67d`.

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:e37096528788f78fb8f9ebe1255c8f16fda1b4f0929180a83d40ec6be9319680` | `ghcr.io/ansible/awx:devel@sha256:e37096528788f78fb8f9ebe1255c8f16fda1b4f0929180a83d40ec6be9319680` | (unchanged) |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | (unchanged) |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake).

Image versions are calver `YYYY.MM.DD` (zero-padded month and day, UTC).
Another cut the same day uses `YYYY.MM.DD-N`, and N starts at 1.

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | keep `0.1.4` | no trigger pin changed |
| `jewel-with-ui` | keep `0.1.4` | no trigger pin changed |
| `awx` | — | skipped (`components.awx.build` is false) |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Set `published.<component>.version` to the UTC calver only for tracks
   whose triggers moved. The first cut that day is `YYYY.MM.DD`. A later
   cut the same day is `2026.10.26-1`, `2026.10.26-2`, and so on.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.10.26 \
  --out release/notes/platform-ui-v2026.10.26.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component is actually released:

1. Bump **only** that image in `awx-platform-operator` → `release/pins.consumer.yaml`.
2. Leave other component pins unchanged.
3. See `release/AGENTS.md`.

