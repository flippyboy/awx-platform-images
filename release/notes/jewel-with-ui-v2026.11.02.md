# jewel-with-ui 2026.11.02

Independent component release. Git tag: `jewel-with-ui-v2026.11.02`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.11.02`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:2026.11.02`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

Built from [`a39b016d5bc6`](https://github.com/ansible/jewel/commit/a39b016d5bc6846a4d6262d4820dbcc91daf355a) with upstream's own Containerfile generator (`scripts/prepare-jewel-context.sh`). The public `ghcr.io/ansible/jewel:latest` image can lag the source.

`docker/jewel/requirements-security.txt` then upgrades packages that upstream still pins at vulnerable versions.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `d45bfa998811 via devel` | `a39b016d5bc6 via devel` | [compare](https://github.com/ansible/jewel/compare/d45bfa9988112739d48ce2e7fda08e0d9d12104a...a39b016d5bc6846a4d6262d4820dbcc91daf355a) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`d45bfa998811` → `a39b016d5bc6` — 3 commits. [compare](https://github.com/ansible/jewel/compare/d45bfa9988112739d48ce2e7fda08e0d9d12104a...a39b016d5bc6846a4d6262d4820dbcc91daf355a)

- [`722defcd6269`](https://github.com/ansible/jewel/commit/722defcd626905370aa7eccfc48eca93512dc9d6) 2026-10-30 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to d29f036 (#320)
- [`1aa46a8bd6bf`](https://github.com/ansible/jewel/commit/1aa46a8bd6bf35c2ee078d0e2a9b98cafd47bfeb) 2026-10-30 [AAP-98757]: Harden migration upgrade CI checks (#303)
- [`a39b016d5bc6`](https://github.com/ansible/jewel/commit/a39b016d5bc6846a4d6262d4820dbcc91daf355a) 2026-10-30 AAP-100207 Remove condition for prepping request.POST in control_plane (#317)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `jewel-with-ui` `2026.11.02` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins jewel to the latest devel tip including CI hardening for migrations and control plane POST handling fixes. Bakes the new platform-ui 2026.11.02. No known issues. Upstream commits serve as the changelog.
