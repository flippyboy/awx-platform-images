# jewel-with-ui 2026.10.29-1

Independent component release. Git tag: `jewel-with-ui-v2026.10.29-1`.

Generated from `pins.yaml` (no pin changes since `jewel-with-ui-v2026.10.29`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.10.29-1`

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
That workflow pins `jewel-with-ui` `2026.10.29-1` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Same-day security recut of `2026.10.29`. Same upstream pins.

The `2026.10.29` image upgraded the venv's pip to 26.2.2, and pip's vendored copies of urllib3 2.7.0, msgpack 1.1.2 and setuptools 70.3.0 brought five high findings back in. Jewel never runs pip at runtime, so this cut removes pip from `/opt/aap_gateway/venv` once the security overrides are installed and `pip check` passes.

Trivy, HIGH and CRITICAL: 0 critical, 2 high. Both need an upstream change:

- lxml 5.3.0 (CVE-2026-41066). xmlsec is built against lxml's libxml2.
- oauthlib 3.3.1 (CVE-2026-49272). The fix is oauthlib 4, and django-oauth-toolkit 2.3 targets oauthlib 3.

