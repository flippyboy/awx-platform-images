# jewel-with-ui 2026.11.16

Independent component release. Git tag: `jewel-with-ui-v2026.11.16`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.11.16`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:2026.11.16`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

Built from [`a89ef1467cfa`](https://github.com/ansible/jewel/commit/a89ef1467cfa8f0e9c5ac931298f10a0695380fa) with upstream's own Containerfile generator (`scripts/prepare-jewel-context.sh`). The public `ghcr.io/ansible/jewel:latest` image can lag the source.

`docker/jewel/requirements-security.txt` then upgrades packages that upstream still pins at vulnerable versions.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `63f7efe90075 via devel` | `a89ef1467cfa via devel` | [compare](https://github.com/ansible/jewel/compare/63f7efe900750b0886ad6b86ee60b6a4aba3058f...a89ef1467cfa8f0e9c5ac931298f10a0695380fa) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`63f7efe90075` → `a89ef1467cfa` — 12 commits. [compare](https://github.com/ansible/jewel/compare/63f7efe900750b0886ad6b86ee60b6a4aba3058f...a89ef1467cfa8f0e9c5ac931298f10a0695380fa)

- [`7fa9631e877f`](https://github.com/ansible/jewel/commit/7fa9631e877f62d4f173c0d075c1576f27f5d673) 2026-11-09 AAP-101727 make keycloak sidecar certs world readable (#339)
- [`d906b5fac836`](https://github.com/ansible/jewel/commit/d906b5fac8363f941e994c96ed4511b3e3f05515) 2026-11-10 [AAP-101688] Split PR Labels concurrency group by event type (#334)
- [`57c39a4ebda4`](https://github.com/ansible/jewel/commit/57c39a4ebda4caec609ce25e89c699a93a47af5b) 2026-11-10 [AAP-101789] Run service_test_app on a current SQLite via sqlean.py (#342)
- [`ae92dbf1ea19`](https://github.com/ansible/jewel/commit/ae92dbf1ea197bf7e916babcc040070b661b5980) 2026-11-10 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to c0d8963 (#341)
- [`78a7f8a402b3`](https://github.com/ansible/jewel/commit/78a7f8a402b37390666f08a202100c01a9a41750) 2026-11-10 AAP-101724 update qemu package name in build and push action (#338)
- [`2135104951fa`](https://github.com/ansible/jewel/commit/2135104951fac2d40f24b1d3fe93f9b3848c8aca) 2026-11-10 [AAP-99638] Add external OAuth bearer authentication (#323)
- [`bd39fdebd78e`](https://github.com/ansible/jewel/commit/bd39fdebd78e252463c80f0fcd2b19e638fa7461) 2026-11-11 [AAP-101049] Set Gateway authentication precedence (#332)
- [`169dbaf65789`](https://github.com/ansible/jewel/commit/169dbaf657895598c052729ed6eeb0429b224a69) 2026-11-11 AAP-101650 Make miscellaneous improvements to the updater CLI (#328)
- [`4171d7e0b5bf`](https://github.com/ansible/jewel/commit/4171d7e0b5bf977595abfc80089253a0d26165c9) 2026-11-12 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 0fb95c8 (#343)
- [`249177dc2275`](https://github.com/ansible/jewel/commit/249177dc22750c81ebdd6e39250298c3fd04b565) 2026-11-12 AAP-102013: Add spec sync (#344)
- [`fee7371893fd`](https://github.com/ansible/jewel/commit/fee7371893fd15d3cc14e4836c1b096a7c75b0c3) 2026-11-12 AAP-101667: Retry upstream connect failures on another node (#345)
- [`a89ef1467cfa`](https://github.com/ansible/jewel/commit/a89ef1467cfa8f0e9c5ac931298f10a0695380fa) 2026-11-12 [AAP-102150] Update python cryptography (#346)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `jewel-with-ui` `2026.11.16` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins jewel to the latest devel tip. Includes security update (python cryptography), external OAuth bearer authentication, gateway auth precedence, retry logic for connect failures, and various CI/test improvements. Bakes the new platform-ui 2026.11.16. No known issues. Upstream commits serve as the changelog.
