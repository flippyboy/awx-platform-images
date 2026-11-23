# platform-ui 2026.11.23

Independent component release. Git tag: `platform-ui-v2026.11.23`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:2026.11.23`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `4552df6e2688 via devel` | `ba68849e3337 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/4552df6e268871c1ab37d9a60c7ddab4a19113cc...ba68849e33371727efc6099231c0644248f0efc1) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `ansible-ui` (`devel`)

`4552df6e2688` → `ba68849e3337` — 10 commits. [compare](https://github.com/ansible/ansible-ui/compare/4552df6e268871c1ab37d9a60c7ddab4a19113cc...ba68849e33371727efc6099231c0644248f0efc1)

- [`b43dbc632330`](https://github.com/ansible/ansible-ui/commit/b43dbc63233017cc21cf0db30375aaa9b7a97782) 2026-11-16 test(platform): Vitest coverage for remaining low-coverage files (AAP-101605) (#3904)
- [`1b7ee96b93c0`](https://github.com/ansible/ansible-ui/commit/1b7ee96b93c0f68c4f1c27f8b9ae030b2b64879a) 2026-11-16 XLAB Add modal for default manual effort and automation creation time (#3832)
- [`7f1564ad77ee`](https://github.com/ansible/ansible-ui/commit/7f1564ad77ee4d13d1d45c622393148fd5e387fb) 2026-11-16 AAP-87097 XLAB Add descriptions to report actions menu (#3866)
- [`2d3d66f92c4a`](https://github.com/ansible/ansible-ui/commit/2d3d66f92c4ac921bd549e4ca9f7e51bb40d4891) 2026-11-17 test(framework): raise Vitest coverage for notifications and dashboard (#3879)
- [`3de85fa50f9d`](https://github.com/ansible/ansible-ui/commit/3de85fa50f9d9f276ce2e89ea52e80b00b355a0e) 2026-11-17 test(awx): Vitest coverage for remaining low-coverage files (AAP-101605) (#3903)
- [`c94afce9db9b`](https://github.com/ansible/ansible-ui/commit/c94afce9db9b80cc2f08e2e19be156f03c3a5710) 2026-11-17 fix: run scheduled visual refresh from Playwright directory (#3907)
- [`a59ecd486db1`](https://github.com/ansible/ansible-ui/commit/a59ecd486db1e7bef9a1453d61e9a0c7bed4cd82) 2026-11-18 AAP-93629 XLAB Fix cleared custom start date overwriting remembered range (#3873)
- [`660d27d2247e`](https://github.com/ansible/ansible-ui/commit/660d27d2247ebd23114ce538d6b5d3a4bd40dd54) 2026-11-18 ci: support scoped packaging App tokens (#3918)
- [`c8fee39dc3c2`](https://github.com/ansible/ansible-ui/commit/c8fee39dc3c26aa11bf82c97ced7a5caa94cdeaf) 2026-11-18 ci: use existing org App credentials for packaging (#3920)
- [`ba68849e3337`](https://github.com/ansible/ansible-ui/commit/ba68849e33371727efc6099231c0644248f0efc1) 2026-11-19 ci: remove packaging PAT fallbacks (#3921)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `platform-ui` `2026.11.23` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins ansible-ui to the latest devel tip. Includes test coverage expansions (Vitest for platform, framework, awx), UI features (modal for default manual effort and automation creation time, descriptions for report actions), fixes (cleared custom start date, scheduled visual refresh), and CI improvements for packaging tokens. No known issues. Upstream commits serve as the changelog.
