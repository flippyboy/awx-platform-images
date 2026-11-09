# jewel-with-ui 2026.11.09

Independent component release. Git tag: `jewel-with-ui-v2026.11.09`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.11.09`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:2026.11.09`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

Built from [`63f7efe90075`](https://github.com/ansible/jewel/commit/63f7efe900750b0886ad6b86ee60b6a4aba3058f) with upstream's own Containerfile generator (`scripts/prepare-jewel-context.sh`). The public `ghcr.io/ansible/jewel:latest` image can lag the source.

`docker/jewel/requirements-security.txt` then upgrades packages that upstream still pins at vulnerable versions.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `a39b016d5bc6 via devel` | `63f7efe90075 via devel` | [compare](https://github.com/ansible/jewel/compare/a39b016d5bc6846a4d6262d4820dbcc91daf355a...63f7efe900750b0886ad6b86ee60b6a4aba3058f) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`a39b016d5bc6` → `63f7efe90075` — 7 commits. [compare](https://github.com/ansible/jewel/compare/a39b016d5bc6846a4d6262d4820dbcc91daf355a...63f7efe900750b0886ad6b86ee60b6a4aba3058f)

- [`6cb5e8599197`](https://github.com/ansible/jewel/commit/6cb5e8599197c6186a22a7915ccf5c58c1f02733) 2026-11-02 AAP-100941 Update oauthlib to 4.0.1 (#321)
- [`661aa0534ac9`](https://github.com/ansible/jewel/commit/661aa0534ac9bb553a8ddf898491b176d0eb5c3e) 2026-11-03 [AAP-100958] Upgrade pyasn1 to 0.6.5 (#324)
- [`fc4cc3f12f74`](https://github.com/ansible/jewel/commit/fc4cc3f12f749fb46a2a1e796ef5fa8c48ecb2c3) 2026-11-04 fix(envoy): Disable X25519MLKEM768 on FIPS (#326)
- [`9705052bda17`](https://github.com/ansible/jewel/commit/9705052bda17753530ad8371c55a5a167d62dae0) 2026-11-05 [Devel] [AAP-96817] Added deprecation headers to existing deprecations (#288)
- [`7fc61e5421a3`](https://github.com/ansible/jewel/commit/7fc61e5421a3f41b4c7019bde0d00ff9f37ab021) 2026-11-06 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to fbbe116 (#330)
- [`1fa6e6c6eec5`](https://github.com/ansible/jewel/commit/1fa6e6c6eec59d9f7fe38b4c3bc1896c095c1ce3) 2026-11-09 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 0557ee8 (#333)
- [`63f7efe90075`](https://github.com/ansible/jewel/commit/63f7efe900750b0886ad6b86ee60b6a4aba3058f) 2026-11-09 Added named to org and team factory (#335)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `jewel-with-ui` `2026.11.09` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins jewel to the latest devel tip. Includes security updates (oauthlib 4.0.1, pyasn1 0.6.5), FIPS-related Envoy fix, deprecation headers, and minor factory/CI updates. Bakes the newly released platform-ui 2026.11.09. No known issues. Upstream commits serve as the changelog.

