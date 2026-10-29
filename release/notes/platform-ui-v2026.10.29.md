# platform-ui 2026.10.29

Independent component release. Git tag: `platform-ui-v2026.10.29`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:2026.10.29`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `48e8281db67d via devel` | `e7017aada0ba via devel` | [compare](https://github.com/ansible/ansible-ui/compare/48e8281db67da5d4a9b63315ee1368d955ed5bc4...e7017aada0ba1334f70699aea58012dcfe4fe60a) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `ansible-ui` (`devel`)

`48e8281db67d` → `e7017aada0ba` — 9 commits. [compare](https://github.com/ansible/ansible-ui/compare/48e8281db67da5d4a9b63315ee1368d955ed5bc4...e7017aada0ba1334f70699aea58012dcfe4fe60a)

- [`1f21cef1abef`](https://github.com/ansible/ansible-ui/commit/1f21cef1abefb47373bb3a8b512ec0e240a32792) 2026-10-26 docs: align PR checklist and skills (#3800)
- [`a2034232bed3`](https://github.com/ansible/ansible-ui/commit/a2034232bed32460d2b44fc5d01d6a629ab38067) 2026-10-26 refactor: remove nested PageFormMultiSelect conditional (#3801)
- [`b08994a2980d`](https://github.com/ansible/ansible-ui/commit/b08994a2980db3474f02efeab3137e28fff03026) 2026-10-26 fix(framework): remove bulk dialog nested ternary (#3656)
- [`a9c008a66f2a`](https://github.com/ansible/ansible-ui/commit/a9c008a66f2ae7eeeabdf662333d5ab69c30d3db) 2026-10-26 test(playwright): stabilize persona session transitions (#3718)
- [`817cdca45a2c`](https://github.com/ansible/ansible-ui/commit/817cdca45a2c4f2aa871775566504fc5f8dddf2c) 2026-10-27 Fix workflow visualizer template swaps with empty extra_data (#3786)
- [`0c1898763ecd`](https://github.com/ansible/ansible-ui/commit/0c1898763ecd72120a4371e14f0bc80ba2eef940) 2026-10-27 fix: stop duplicating workflow node job tags (AAP-65215) (#3705)
- [`d950efccaa5f`](https://github.com/ansible/ansible-ui/commit/d950efccaa5f8b3754d73801887e74167f115bc8) 2026-10-27 test: add SingleSelect typeahead safety net (#3787)
- [`20d4a69dd178`](https://github.com/ansible/ansible-ui/commit/20d4a69dd178647ce664788e2790368a68b14fbb) 2026-10-27 chore: remove stale page details lint disables (#3805)
- [`e7017aada0ba`](https://github.com/ansible/ansible-ui/commit/e7017aada0ba1334f70699aea58012dcfe4fe60a) 2026-10-27 AAP-98253: Show authenticator mapping attribute validation errors on form fields (#3831)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `platform-ui` `2026.10.29` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

First calendar-version cut, and a security release.

- The runtime moves from `nginx:1.27-alpine` to `nginx:1.30-alpine` (Alpine 3.24). 1.27 is end of life, and its Alpine 3.21.3 base was no longer rebuilt.
- `apk upgrade` runs at build time, so Alpine fixes published after the base image apply.

Trivy, HIGH and CRITICAL: 0.1.4 had 3 critical and 57 high, all in Alpine packages (openssl, curl, libexpat, libxml2, musl, zlib and others). This build has none.

