# jewel-with-ui 2026.10.29

Independent component release. Git tag: `jewel-with-ui-v2026.10.29`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:2026.10.29`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:2026.10.29`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

Built from [`d45bfa998811`](https://github.com/ansible/jewel/commit/d45bfa9988112739d48ce2e7fda08e0d9d12104a) with upstream's own Containerfile generator (`scripts/prepare-jewel-context.sh`). The public `ghcr.io/ansible/jewel:latest` image can lag the source.

`docker/jewel/requirements-security.txt` then upgrades packages that upstream still pins at vulnerable versions.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `f664db1b715e via devel` | `d45bfa998811 via devel` | [compare](https://github.com/ansible/jewel/compare/f664db1b715e95b5f8f31b28b4bd724f73bc43cb...d45bfa9988112739d48ce2e7fda08e0d9d12104a) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`f664db1b715e` → `d45bfa998811` — 3 commits. [compare](https://github.com/ansible/jewel/compare/f664db1b715e95b5f8f31b28b4bd724f73bc43cb...d45bfa9988112739d48ce2e7fda08e0d9d12104a)

- [`ce55bd02222b`](https://github.com/ansible/jewel/commit/ce55bd02222b8813322aa7a1cef64718fe1a9b13) 2026-10-27 [AAP-99907] Fix git auth failure in migration upgrade CI (#313)
- [`29a0cddb679e`](https://github.com/ansible/jewel/commit/29a0cddb679e9f2748710f87afa60ff2342f2b9a) 2026-10-28 AAP-95746 Bump DVCS check commit (#309)
- [`d45bfa998811`](https://github.com/ansible/jewel/commit/d45bfa9988112739d48ce2e7fda08e0d9d12104a) 2026-10-28 AAP-95746 Update DVCS check to authenticate when reading PR (#315)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `jewel-with-ui` `2026.10.29` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

First calendar-version cut, and a security release.

The upstream `ghcr.io/ansible/jewel:latest` image has not been republished since 2026-10-22. Upstream's image workflow fails on the Ubuntu 26.04 runners, where `qemu-user-static` is no longer installable. So the 0.1.4 image shipped Django REST framework 3.15.2 even though jewel `f664db1` already required 3.18.2 or later. This release builds Jewel from the pinned commit instead (`components.jewel.build: true`). That picks up Django REST framework 3.18.3 and the django-ansible-base change that lifted its `<3.16` pin.

`docker/jewel/requirements-security.txt` then upgrades what upstream still pins at vulnerable versions: Django 5.2.18 (5.2 LTS), cryptography 50.0.2, certifi 2026.10.23, protobuf 5.29.6, setuptools 84.2.1, idna 3.15, PyJWT 2.15.1 and pip 26.2.2. `pip check`, `manage.py check` and `makemigrations --check` pass.

Trivy, HIGH and CRITICAL: 0.1.4 had 1 critical and 17 high. Two high findings remain, and both need an upstream change:

- lxml 5.3.0 (CVE-2026-41066). xmlsec is built against lxml's libxml2, so lxml 6 needs a matching xmlsec.
- oauthlib 3.3.1 (CVE-2026-49272). The fix is oauthlib 4, and django-oauth-toolkit 2.3 targets oauthlib 3.

