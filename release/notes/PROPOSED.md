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
| awx | `e995e5fc5f92 via devel` | `33a9eb7d15ae via devel` | [compare](https://github.com/ansible/awx/compare/e995e5fc5f925078aab296acda5acb1df39b49d0...33a9eb7d15aedca7222354b68cde834480415913) |
| jewel | `e680bd860a58 via devel` | `a5e20b5361f6 via devel` | [compare](https://github.com/ansible/jewel/compare/e680bd860a58db23380c0b12807d31cab71856ef...a5e20b5361f61836e80c8eb4191615fff0d3e527) |
| ansible-ui | `4c3403d95196 via devel` | `8651d9537708 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/4c3403d951965d7d0527926f564a122588ef9ece...8651d9537708923684306b5e9a782ac03e46af43) |

**3** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

`e995e5fc5f92` → `33a9eb7d15ae` — 3 commits. [compare](https://github.com/ansible/awx/compare/e995e5fc5f925078aab296acda5acb1df39b49d0...33a9eb7d15aedca7222354b68cde834480415913)

- [`3c76e236c270`](https://github.com/ansible/awx/commit/3c76e236c270b831f0f71465c3e0d7fae040c83a) 2026-09-30 [AAP-93690] Add CleanText validation and OPTIONS patterns to subscription wizard (#16671)
- [`e4a42b0399a9`](https://github.com/ansible/awx/commit/e4a42b0399a929586060a55e2fac4f8d0ec85f68) 2026-10-02 [AAP-93983] Update schema to add pattern fields for credential types (#16670)
- [`33a9eb7d15ae`](https://github.com/ansible/awx/commit/33a9eb7d15aedca7222354b68cde834480415913) 2026-10-02 Pin ruff to a compatible release (~=0.16.0) (#16694)

### `jewel` (`devel`)

`e680bd860a58` → `a5e20b5361f6` — 8 commits. [compare](https://github.com/ansible/jewel/compare/e680bd860a58db23380c0b12807d31cab71856ef...a5e20b5361f61836e80c8eb4191615fff0d3e527)

- [`c0e9eb96e981`](https://github.com/ansible/jewel/commit/c0e9eb96e9811afb28dccd72ee28f74e0c9d0266) 2026-09-30 [AAP-65516] Removing POST option from service_keys endpoint (#235)
- [`e09ebeded951`](https://github.com/ansible/jewel/commit/e09ebeded951db1e25211d682ecde488855d98b7) 2026-10-01 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 9fe7ebd (#261)
- [`9d11a9fe110c`](https://github.com/ansible/jewel/commit/9d11a9fe110c73f06c6a8a4ae26f88020eb18c54) 2026-10-01 test: exclude bulk-update endpoint from test_request_objects (#262)
- [`0f1b90f9f39a`](https://github.com/ansible/jewel/commit/0f1b90f9f39ac1bdd314b5f49c5e6b50312f3799) 2026-10-01 [AAP-95395] Upgrade PyJWT to safe version (#263)
- [`fbcb9fbe8c19`](https://github.com/ansible/jewel/commit/fbcb9fbe8c195331859da8b9c235c48a4ba310d4) 2026-10-02 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to bd27a48 (#265)
- [`b9ce7e85eb78`](https://github.com/ansible/jewel/commit/b9ce7e85eb78d9069fe54c4e8d1090ac308b4d86) 2026-10-02 fix(envoy): redirect bare API and service paths to trailing slashes (#234)
- [`6a4a37fe85f8`](https://github.com/ansible/jewel/commit/6a4a37fe85f81e1e6471487e0739d9a65d5809fe) 2026-10-02 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to a4ab29e (#266)
- [`a5e20b5361f6`](https://github.com/ansible/jewel/commit/a5e20b5361f61836e80c8eb4191615fff0d3e527) 2026-10-02 [AAP-38240] Migrate development environment to Podman (#245)

### `ansible-ui` (`devel`)

`4c3403d95196` → `8651d9537708` — 16 commits. [compare](https://github.com/ansible/ansible-ui/compare/4c3403d951965d7d0527926f564a122588ef9ece...8651d9537708923684306b5e9a782ac03e46af43)

- [`43511b0941e1`](https://github.com/ansible/ansible-ui/commit/43511b0941e119c564a50bc7118c776494640802) 2026-09-29 Apply OPTIONS normalize before client-side pattern validation (#3668)
- [`59952921771c`](https://github.com/ansible/ansible-ui/commit/59952921771c43bcf1746c5edc67549100f0cb03) 2026-09-29 fix(data-editor): keep YAML parse errors visible after blur (AAP-93178) (#3670)
- [`351242745b55`](https://github.com/ansible/ansible-ui/commit/351242745b55560cb852e0de2d0404d1a82a4957) 2026-09-30 fix(e2e): wait for Controller org sync only in Organization helper (#3681)
- [`8b2817af69f5`](https://github.com/ansible/ansible-ui/commit/8b2817af69f5e99ee55ffffab694f7b89531470b) 2026-10-01 fix(awx): sync job status links for inventory and project resources  (#3667)
- [`100227d81df8`](https://github.com/ansible/ansible-ui/commit/100227d81df84ef61c5e4d89687c982b802a7330) 2026-10-01 Check for signed commits on PR (#3664)
- [`b38935baed45`](https://github.com/ansible/ansible-ui/commit/b38935baed450481b0305d999eb13830c759d91f) 2026-10-01 Fix RevertAllDialog vitest focus-trap (follow-up to #3648) (#3688)
- [`79e4ceb86c55`](https://github.com/ansible/ansible-ui/commit/79e4ceb86c556daf07c5ffb34fcb62b2c47b19c3) 2026-10-01 fix(AAP-94066): harden PageWizard supplemental merge and launch config wait (#3640)
- [`2b72cc7c917d`](https://github.com/ansible/ansible-ui/commit/2b72cc7c917dd2aefc31a1fed61f4b3bc839b572) 2026-10-01 Use js-yaml for RequestError details (#3637)
- [`3e0ec798484e`](https://github.com/ansible/ansible-ui/commit/3e0ec798484ec700f7baccd2a5d5a3b4beeb09f8) 2026-10-01 fix: support Gateway float settings type (AAP-61719) (#3593)
- [`d1d5f1d536ab`](https://github.com/ansible/ansible-ui/commit/d1d5f1d536aba42e247532c77134f97b236c6eb0) 2026-10-01 feat: consume JSON sub-key validation patterns in UI forms (#3602)
- [`18e2cc0212b5`](https://github.com/ansible/ansible-ui/commit/18e2cc0212b59c0ba7949953a02db8948dc18f8e) 2026-10-01 Replace type-fest with local utility types (#3638)
- [`9ec99fe76d56`](https://github.com/ansible/ansible-ui/commit/9ec99fe76d560385f2c8dadd50d503fc9f392a37) 2026-10-02 [ANSTRAT-1976] Automation Dashboard Gamification UI (#3694)
- [`e8aed44768fb`](https://github.com/ansible/ansible-ui/commit/e8aed44768fb1ee40a32462a008cca00ce9f98b3) 2026-10-02 fix(test): migrate unit tests from fireEvent to userEvent (#3628)
- [`9ccc3ff902a4`](https://github.com/ansible/ansible-ui/commit/9ccc3ff902a43e78f91710f9bf3614d4483b5014) 2026-10-02 fix(e2e): restore org link on manage-roles and stabilize host bulk delete (#3682)
- [`f5876d59841b`](https://github.com/ansible/ansible-ui/commit/f5876d59841b2ec37b771e0dce57d95efc6d38a4) 2026-10-02 fix(inventories): support labels on constructed inventories (#3573)
- [`8651d9537708`](https://github.com/ansible/ansible-ui/commit/8651d9537708923684306b5e9a782ac03e46af43) 2026-10-02 [AAP-95233] Fix Job Activity chart clipping current day (#3693)

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:ae94fd1b7a17d22cd51e60919b4cfe78c549b9e1355aefac776a7d06c651ed3c` | `ghcr.io/ansible/awx:devel@sha256:010c34221b3fa698e5138fddb911dc23b14901cf122500166c518958fa8e8db6` | development tag; stable versions are not used |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:ed49c4cbd073eea03914913088fc97d75dcb4628651ca8d1a29b2c8258675ca0` | `ghcr.io/ansible/jewel:latest@sha256:be550b2827c665f2eeda789cec8d146ecc19f47f735f223d459c8e97c85020d9` | development tag; stable versions are not used |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake):

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v0.1.3` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v0.1.3` | upstream moved: `jewel` |
| `awx` | — | upstream moved, but `components.awx.build` is false — record the digest, do not cut an awx image |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Bump `published.<component>.version` only for tracks whose triggers moved.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version X.Y.Z \
  --out release/notes/platform-ui-vX.Y.Z.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component is actually released:

1. Bump **only** that image in `awx-platform-operator` → `release/pins.consumer.yaml`.
2. Leave other component pins unchanged.
3. See `release/AGENTS.md`.

