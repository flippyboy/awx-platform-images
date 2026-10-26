# jewel-with-ui 0.1.4

Independent component release. Git tag: `jewel-with-ui-v0.1.4`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:0.1.4`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:0.1.4`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

`ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d`

Development image (`latest` / `devel`). A pinned digest is what the release build pulls. Stable upstream version tags are not used.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `b9eb41abe310 via devel` | `f664db1b715e via devel` | [compare](https://github.com/ansible/jewel/compare/b9eb41abe31025e6a3c27fe25c36007a12de877d...f664db1b715e95b5f8f31b28b4bd724f73bc43cb) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`b9eb41abe310` → `f664db1b715e` — 7 commits. [compare](https://github.com/ansible/jewel/compare/b9eb41abe31025e6a3c27fe25c36007a12de877d...f664db1b715e95b5f8f31b28b4bd724f73bc43cb)

- [`5755b60c995e`](https://github.com/ansible/jewel/commit/5755b60c995ef6e246862896bb49ec16208dcbf4) 2026-10-20 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 198dcb6 (#299)
- [`55414d0633c0`](https://github.com/ansible/jewel/commit/55414d0633c0300b9568db19de9eb9070a07ea14) 2026-10-21 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 5b28951 (#302)
- [`be6dedbe1b78`](https://github.com/ansible/jewel/commit/be6dedbe1b7895ab1a0a8d7db2a5de3b0174b06c) 2026-10-22 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 9969c1e (#304)
- [`ba98bb9ee0d1`](https://github.com/ansible/jewel/commit/ba98bb9ee0d1269d91d3aa02c6d5fc7a809cfb41) 2026-10-22 AAP-95746 Drop write permissions from DVCS check (#305)
- [`b9ab5e463181`](https://github.com/ansible/jewel/commit/b9ab5e4631814ee2d7beb0e7e0f02d2e273cfa98) 2026-10-22 Revert "AAP-95746 Drop write permissions from DVCS check (#305)" (#308)
- [`2523f136f6d4`](https://github.com/ansible/jewel/commit/2523f136f6d4dff953ba6648e3571615685636f3) 2026-10-26 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 032d2d9 (#311)
- [`f664db1b715e`](https://github.com/ansible/jewel/commit/f664db1b715e95b5f8f31b28b4bd724f73bc43cb) 2026-10-26 AAP-99716 Upgrade django-rest-framework to >= 3.18.2 (#312)

## Operator handoff

1. Bump **only** `jewel-with-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.4` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
4. Cut an operator release only when the operator itself or chart defaults need a ship.

## Notes

jewel `devel` moved 7 commits past the 0.1.3 pin (`b9eb41abe310` → `f664db1b715e`). This cut follows that tip and bakes the new platform-ui 0.1.4. Notable: Django REST framework upgrade, various test image digest updates, and a temporary permission change that was reverted. The commit list above is the full changelog.
