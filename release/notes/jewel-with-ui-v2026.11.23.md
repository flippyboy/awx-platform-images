# jewel-with-ui 2026.11.23

Independent component release. Git tag: `jewel-with-ui-v2026.11.23`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.11.23`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:2026.11.23`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

Built from [`0438448e3787`](https://github.com/ansible/jewel/commit/0438448e3787ca26ae31a16ebd527f1b2ef152e8) with upstream's own Containerfile generator (`scripts/prepare-jewel-context.sh`). The public `ghcr.io/ansible/jewel:latest` image can lag the source.

`docker/jewel/requirements-security.txt` then upgrades packages that upstream still pins at vulnerable versions.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `a89ef1467cfa via devel` | `0438448e3787 via devel` | [compare](https://github.com/ansible/jewel/compare/a89ef1467cfa8f0e9c5ac931298f10a0695380fa...0438448e3787ca26ae31a16ebd527f1b2ef152e8) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`a89ef1467cfa` → `0438448e3787` — 6 commits. [compare](https://github.com/ansible/jewel/compare/a89ef1467cfa8f0e9c5ac931298f10a0695380fa...0438448e3787ca26ae31a16ebd527f1b2ef152e8)

- [`cf64664bb59c`](https://github.com/ansible/jewel/commit/cf64664bb59ccae4dfb4cbf9cc85faa0817a4d1b) 2026-11-18 AAP-91965 Add the jewel caller workflow for approval label auth (#347)
- [`b368c6a3b76a`](https://github.com/ansible/jewel/commit/b368c6a3b76ad5c90681f8309fca4aab39bca5b8) 2026-11-21 AAP-102564 Apply local DAB branch dependency changes in tox and dev environment (#352)
- [`47371535a10f`](https://github.com/ansible/jewel/commit/47371535a10fd4527c0bdfcb937e82544b989e1e) 2026-11-21 AAP-77767 Make xds information hidden from requests to envoy (#350)
- [`824a54bcf342`](https://github.com/ansible/jewel/commit/824a54bcf3420099c631581026c9d0f31d370d2e) 2026-11-23 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 455e3cc (#358)
- [`61ac9c95cf41`](https://github.com/ansible/jewel/commit/61ac9c95cf41df4ea5e50d525696b02805e8c9a2) 2026-11-23 [AAP-86435] Add API contract CI workflows (#353)
- [`0438448e3787`](https://github.com/ansible/jewel/commit/0438448e3787ca26ae31a16ebd527f1b2ef152e8) 2026-11-23 AAP-77767 Add opt-in API endpoint hardening controls, deprecate some ping fields (#356)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `jewel-with-ui` `2026.11.23` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins jewel to the latest devel tip. Includes approval label auth workflow, local DAB dependency updates, API endpoint hardening controls (opt-in, deprecating some ping fields), API contract CI workflows, and test digest updates. Bakes the new platform-ui 2026.11.23. No known issues. Upstream commits serve as the changelog.
