# jewel-with-ui 2026.10.29-2

Independent component release. Git tag: `jewel-with-ui-v2026.10.29-2`.

Generated from `pins.yaml` (no pin changes since `jewel-with-ui-v2026.10.29-1`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.10.29-2`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:2026.10.29`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

Built from [`d45bfa998811`](https://github.com/ansible/jewel/commit/d45bfa9988112739d48ce2e7fda08e0d9d12104a) with upstream's own Containerfile generator (`scripts/prepare-jewel-context.sh`). The public `ghcr.io/ansible/jewel:latest` image can lag the source.

`docker/jewel/requirements-security.txt` then upgrades packages that upstream still pins at vulnerable versions.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `d45bfa998811 via devel` | `d45bfa998811 via devel` | (unchanged) |

**0** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

Unchanged at `d45bfa998811`.

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `jewel-with-ui` `2026.10.29-2` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Security recut of `2026.10.29-1`. Same upstream pins.

Upstream's `/usr/bin/launch-gateway`, a development-environment script, prints the admin password to stdout on every gateway start (`>>>>>>>> Admin password: ...`). The upstream `ghcr.io/ansible/jewel` image ships the same script, so every earlier jewel-with-ui release logged it too. The build now replaces that line with `Admin password set from the mounted secret`, and fails if any line still echoes the password.

**Rotate the admin password** on every installation that ran an earlier image, if anyone else can read the gateway's logs or the logs were shipped anywhere.

Trivy, HIGH and CRITICAL: unchanged from `2026.10.29-1` (0 critical, 2 high: lxml and oauthlib).

