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
| awx | `6fc51b6d25b5 via devel` | `edabe5d6eb7d via devel` | [compare](https://github.com/ansible/awx/compare/6fc51b6d25b5bf3ad7efa66cc4e62bdb27177027...edabe5d6eb7d89c87a933dbd51fa28dcc7ca3a0e) |
| jewel | `b9eb41abe310 via devel` | `f664db1b715e via devel` | [compare](https://github.com/ansible/jewel/compare/b9eb41abe31025e6a3c27fe25c36007a12de877d...f664db1b715e95b5f8f31b28b4bd724f73bc43cb) |
| ansible-ui | `78bde81bc413 via devel` | `48e8281db67d via devel` | [compare](https://github.com/ansible/ansible-ui/compare/78bde81bc413d092b60052b336aee06eb60e3d3c...48e8281db67da5d4a9b63315ee1368d955ed5bc4) |

**3** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

`6fc51b6d25b5` → `edabe5d6eb7d` — 6 commits. [compare](https://github.com/ansible/awx/compare/6fc51b6d25b5bf3ad7efa66cc4e62bdb27177027...edabe5d6eb7d89c87a933dbd51fa28dcc7ca3a0e)

- [`a17f5c167b24`](https://github.com/ansible/awx/commit/a17f5c167b24b8639baa7c5fc5841d6a7e3e6bcb) 2026-10-21 Add SSRF egress filtering and allowlist to notification backends (#16679)
- [`85c334e3a447`](https://github.com/ansible/awx/commit/85c334e3a4476a77f4680aa1c009442080f3d7b9) 2026-10-22 AAP-96178: Fix unified_jobs pagination count to respect RBAC filtering (#16751)
- [`c9b547d6d950`](https://github.com/ansible/awx/commit/c9b547d6d950618650106377e40d3a29fed5bb90) 2026-10-22 fix: do not call .filter() on list before converting to queryset (#16752)
- [`b2a3c87b4696`](https://github.com/ansible/awx/commit/b2a3c87b46961da868e89046e65759c870889aa9) 2026-10-23 Remove EE container after awx-manage inventory_import
- [`e9ad2414165f`](https://github.com/ansible/awx/commit/e9ad2414165f275aed499584fdfc5283400ed2c0) 2026-10-23 Stop using floating Python 3.x in docs and label_pr CI (#16753)
- [`edabe5d6eb7d`](https://github.com/ansible/awx/commit/edabe5d6eb7d89c87a933dbd51fa28dcc7ca3a0e) 2026-10-23 Migrate from deprecated _actor_role_filter to actor_role_ids (#16750)

### `jewel` (`devel`)

`b9eb41abe310` → `f664db1b715e` — 7 commits. [compare](https://github.com/ansible/jewel/compare/b9eb41abe31025e6a3c27fe25c36007a12de877d...f664db1b715e95b5f8f31b28b4bd724f73bc43cb)

- [`5755b60c995e`](https://github.com/ansible/jewel/commit/5755b60c995ef6e246862896bb49ec16208dcbf4) 2026-10-20 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 198dcb6 (#299)
- [`55414d0633c0`](https://github.com/ansible/jewel/commit/55414d0633c0300b9568db19de9eb9070a07ea14) 2026-10-21 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 5b28951 (#302)
- [`be6dedbe1b78`](https://github.com/ansible/jewel/commit/be6dedbe1b7895ab1a0a8d7db2a5de3b0174b06c) 2026-10-22 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 9969c1e (#304)
- [`ba98bb9ee0d1`](https://github.com/ansible/jewel/commit/ba98bb9ee0d1269d91d3aa02c6d5fc7a809cfb41) 2026-10-22 AAP-95746 Drop write permissions from DVCS check (#305)
- [`b9ab5e463181`](https://github.com/ansible/jewel/commit/b9ab5e4631814ee2d7beb0e7e0f02d2e273cfa98) 2026-10-22 Revert "AAP-95746 Drop write permissions from DVCS check (#305)" (#308)
- [`2523f136f6d4`](https://github.com/ansible/jewel/commit/2523f136f6d4dff953ba6648e3571615685636f3) 2026-10-26 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 032d2d9 (#311)
- [`f664db1b715e`](https://github.com/ansible/jewel/commit/f664db1b715e95b5f8f31b28b4bd724f73bc43cb) 2026-10-26 AAP-99716 Upgrade django-rest-framework to >= 3.18.2 (#312)

### `ansible-ui` (`devel`)

`78bde81bc413` → `48e8281db67d` — 22 commits. [compare](https://github.com/ansible/ansible-ui/compare/78bde81bc413d092b60052b336aee06eb60e3d3c...48e8281db67da5d4a9b63315ee1368d955ed5bc4)

- [`ec3a8b524122`](https://github.com/ansible/ansible-ui/commit/ec3a8b524122ad3933b3eb6a580596b14e4559d7) 2026-10-19 fix(access): team assign search uses starts-with filter (#3766)
- [`a82fd31be02a`](https://github.com/ansible/ansible-ui/commit/a82fd31be02a76de30dbbe40cc7cea4ec4acdc4e) 2026-10-19 Revert #3589 (#3784)
- [`6e1fa4c43beb`](https://github.com/ansible/ansible-ui/commit/6e1fa4c43beb07ee3326c27c8638a56514a9341e) 2026-10-20 AAP-87021 XLAB Keep Monthly AAP cost edits from being discarded (#3765)
- [`410e4c0b9f69`](https://github.com/ansible/ansible-ui/commit/410e4c0b9f690cd8603f4eec8d9ffedbfba505ab) 2026-10-20 test: stabilize bulk action dialog close timing (#3754)
- [`778e6637c30c`](https://github.com/ansible/ansible-ui/commit/778e6637c30c18cb20707763a64c454c302dad58) 2026-10-20 fix(notifications): allow org auditors to access notification tab (#3547)
- [`43293efe05fd`](https://github.com/ansible/ansible-ui/commit/43293efe05fd61cd615bc0f3f118ed4a288a5aef) 2026-10-20 AAP-95614: dedupe workflow node labels on edit (#3733)
- [`a860875264e2`](https://github.com/ansible/ansible-ui/commit/a860875264e21d422efb967726cb25a6795ef89c) 2026-10-20 AAP-95975: omit unchanged UJT on workflow node save (#3732)
- [`f3f49ff58044`](https://github.com/ansible/ansible-ui/commit/f3f49ff580446fd0b45a105b2c811f7a8603e7c3) 2026-10-20 remove success toast (#3807)
- [`814b83bf1896`](https://github.com/ansible/ansible-ui/commit/814b83bf1896458e30b4a18135e23911749beccc) 2026-10-21 test: add MultiSelect typeahead safety net (#3788)
- [`a7f6ebf97d9e`](https://github.com/ansible/ansible-ui/commit/a7f6ebf97d9ea7598c37d9b04d2a5d6799a95abe) 2026-10-21 chore(deps): update react-hook-form to v7.90 (#3775)
- [`4923b42098dc`](https://github.com/ansible/ansible-ui/commit/4923b42098dc894cfaf2f769989ec8584068db85) 2026-10-21 AAP-95614: test workflow node label merge on launch config reload (#3809)
- [`26a76f0f0897`](https://github.com/ansible/ansible-ui/commit/26a76f0f089787b27ecdbeeb1816945326c2f457) 2026-10-21 chore: add React effect guardrail plugin (#3727)
- [`0e74e9a6526e`](https://github.com/ansible/ansible-ui/commit/0e74e9a6526e7f3582e10623df906f3c7a69edac) 2026-10-21 fix(awx): include the job id when downloading a job log (AAP-97735) (#3774)
- [`2622bee85608`](https://github.com/ansible/ansible-ui/commit/2622bee85608b29834770db776c55fe597e76f2f) 2026-10-21 Fix for changing jobs table to 100 per page removes pagination controls (#3748)
- [`08f1ccdac573`](https://github.com/ansible/ansible-ui/commit/08f1ccdac573d18aec7767324d63d932d1525a73) 2026-10-21 fix: sync org rename to controller and stabilize workflow viz tier1 E2E (#3806)
- [`0f7c5b1cee08`](https://github.com/ansible/ansible-ui/commit/0f7c5b1cee08f944aadff0e051af85b9e4352640) 2026-10-22 fix(common): keep spaces in search when navigating back to a list (AAP-80966) (#3772)
- [`cabb51c17194`](https://github.com/ansible/ansible-ui/commit/cabb51c1719403b76458253ec14e06821ec7465b) 2026-10-22 feat(access): prefer authenticator plugin display_name (AAP-98600) (#3799)
- [`8debee7eb36a`](https://github.com/ansible/ansible-ui/commit/8debee7eb36a5fed094bbd20cda156296ebb472e) 2026-10-22 fix(AAP-95614): dedupe workflow prompt tags and show JT instance groups (#3811)
- [`e61b1c0b6a55`](https://github.com/ansible/ansible-ui/commit/e61b1c0b6a554cb31695b153e7ba3c6b4334197f) 2026-10-22 fix(awx): allow extra credential types on workflow nodes (AAP-74107) (#3773)
- [`69b6d5e7d5b2`](https://github.com/ansible/ansible-ui/commit/69b6d5e7d5b2e5c5525414fef2ff28bbdd098e4c) 2026-10-22 fix(framework): let Page detect small viewports so the nav can open (… (#3821)
- [`a5cf27d5eb6b`](https://github.com/ansible/ansible-ui/commit/a5cf27d5eb6bf6dcdd416af9b1343e68501c0268) 2026-10-22 chore(ci): remove Publish Framework workflow (#3737)
- [`48e8281db67d`](https://github.com/ansible/ansible-ui/commit/48e8281db67da5d4a9b63315ee1368d955ed5bc4) 2026-10-23 hosts automated help text change (#3824)

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:fc3f70c98976f76add3a932844b3c62ad7df373de11f85ba043dd261ae9e7a95` | `ghcr.io/ansible/awx:devel@sha256:e37096528788f78fb8f9ebe1255c8f16fda1b4f0929180a83d40ec6be9319680` | development tag; stable versions are not used |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:748fcc338ea3d651601903070bc104bd11a890514cf091da6e46a6be54171ed7` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | development tag; stable versions are not used |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake):

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v0.1.4` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v0.1.4` | upstream moved: `jewel` |
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

