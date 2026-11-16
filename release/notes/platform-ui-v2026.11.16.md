# platform-ui 2026.11.16

Independent component release. Git tag: `platform-ui-v2026.11.16`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:2026.11.16`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `6ebe395827b2 via devel` | `4552df6e2688 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/6ebe395827b2a20594233d23333613ff2ef6172c...4552df6e268871c1ab37d9a60c7ddab4a19113cc) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `ansible-ui` (`devel`)

`6ebe395827b2` → `4552df6e2688` — 13 commits. [compare](https://github.com/ansible/ansible-ui/compare/6ebe395827b2a20594233d23333613ff2ef6172c...4552df6e268871c1ab37d9a60c7ddab4a19113cc)

- [`95e5f717ef9b`](https://github.com/ansible/ansible-ui/commit/95e5f717ef9b06db30a7247e7208bbdd07fb7897) 2026-11-10 fix(playwright): resolve EDA organization for SCM project tests (#3884)
- [`7903fd3db8be`](https://github.com/ansible/ansible-ui/commit/7903fd3db8be2fc90fd953584089ca93674d53aa) 2026-11-10 chore(deps): update i18n packages (#3780)
- [`ca90bd982f0a`](https://github.com/ansible/ansible-ui/commit/ca90bd982f0a79315f25c5cb11de65a703bd1809) 2026-11-10 test: expand deterministic visual regression coverage (#3803)
- [`ab44f22d76d4`](https://github.com/ansible/ansible-ui/commit/ab44f22d76d4dea4e601cc27ad70dad0d3054bd6) 2026-11-11 feat(platform): make application display name configurable (#3889)
- [`8280920ef490`](https://github.com/ansible/ansible-ui/commit/8280920ef490f5f7dd2151cd8708c9e41c2ed9f2) 2026-11-11 refactor: simplify page header conditional (#3792)
- [`c1f9e565185a`](https://github.com/ansible/ansible-ui/commit/c1f9e565185ab5b141fab7744d8e9eb5806cf1ac) 2026-11-11 refactor: flatten async multi-select validation conditional (#3797)
- [`98eab333cf52`](https://github.com/ansible/ansible-ui/commit/98eab333cf52091a8f8e0cafa5ca55643a1db294) 2026-11-12 chore(deps): update SWR and Zustand (#3781)
- [`c32cf21d6372`](https://github.com/ansible/ansible-ui/commit/c32cf21d6372dbf12a254b58c5838fc0b0726cdb) 2026-11-12 test(platform): expand access Vitest coverage (AAP-101605) (#3877)
- [`09023dd23936`](https://github.com/ansible/ansible-ui/commit/09023dd239360299937ffddbd253bad0fbb40955) 2026-11-12 test(frontend): Vitest coverage toward 90% per file (AAP-101605) (#3886)
- [`a92ee52d81ad`](https://github.com/ansible/ansible-ui/commit/a92ee52d81ad1c91c9e98915c21d7d19e18dbf8b) 2026-11-12 fix(awx): use hostname values for node filters and include hybrid nodes (#3888)
- [`6b42d498156b`](https://github.com/ansible/ansible-ui/commit/6b42d498156b836da6c4054b075d981f81f24d1b) 2026-11-13 feat(platform): use application name in overview description (#3899)
- [`1b9496dbc6df`](https://github.com/ansible/ansible-ui/commit/1b9496dbc6dff8f423fd9ea14b84804d78b0ed78) 2026-11-13 refactor: remove nested PageFormSingleSelect conditional (#3802)
- [`4552df6e2688`](https://github.com/ansible/ansible-ui/commit/4552df6e268871c1ab37d9a60c7ddab4a19113cc) 2026-11-16 [AAP-95513] Preserve dashboard filters in Controller job links (#3898)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `platform-ui` `2026.11.16` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins ansible-ui to the latest devel tip. Includes features (configurable application display name, preserve dashboard filters in job links), dependency updates (i18n, SWR, Zustand), test coverage expansions, and various refactors/fixes. No known issues. Upstream commits serve as the changelog.
