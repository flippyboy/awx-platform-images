# Proposed pin update

Proposal for the next **pinned** image release. Upstream stable and semver
tags are not candidates — those releases lag the branches where new features
land (`devel`, or `main` when that is the development branch).

Each git pin is that branch's tip commit. Each public image pin is the
registry digest of the floating development tag (`devel` / `latest`), not a
stable version tag.

**Review before merge.** This is the input for cutting a release, not the release.

Generated from pin delta (`pins.prev.yaml` → `pins.proposed.yaml`).

## Upstream pins

| Upstream | Previous | Proposed | Link |
|----------|----------|----------|------|
| awx | `d4159cab745d via devel` | `7de482b075ef via devel` | [compare](https://github.com/ansible/awx/compare/d4159cab745d1fa6e2247bf3cf7aae4b0546f1b3...7de482b075ef78add0f49b04b26f24bf0fd5a14b) |
| jewel | `63f7efe90075 via devel` | `a89ef1467cfa via devel` | [compare](https://github.com/ansible/jewel/compare/63f7efe900750b0886ad6b86ee60b6a4aba3058f...a89ef1467cfa8f0e9c5ac931298f10a0695380fa) |
| ansible-ui | `6ebe395827b2 via devel` | `4552df6e2688 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/6ebe395827b2a20594233d23333613ff2ef6172c...4552df6e268871c1ab37d9a60c7ddab4a19113cc) |

**3** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

`d4159cab745d` → `7de482b075ef` — 7 commits. [compare](https://github.com/ansible/awx/compare/d4159cab745d1fa6e2247bf3cf7aae4b0546f1b3...7de482b075ef78add0f49b04b26f24bf0fd5a14b)

- [`f1bf5721718b`](https://github.com/ansible/awx/commit/f1bf5721718b4213145e66bc81f9a376e0053483) 2026-11-10 [Devel] [AAP-96816] Add New Deprecation Mechanisms To Existing Deprectations (#16771)
- [`b970bf20255b`](https://github.com/ansible/awx/commit/b970bf20255b6782fc4daccf81e7ee6d4a4dd174) 2026-11-12 [Devel] Add Deprecation Detail In Browsable API Banner (#16777)
- [`798f71b7f9ce`](https://github.com/ansible/awx/commit/798f71b7f9cefbe5c4e27bfe47cbec6b610f1915) 2026-11-13 AAP-91965 Add approval label authorization caller workflow (#16762)
- [`c5c89639aa3a`](https://github.com/ansible/awx/commit/c5c89639aa3a992efe2f2e103f5a114f925334df) 2026-11-13 fix: update aiohttp version (#16802)
- [`5be49a25ea4a`](https://github.com/ansible/awx/commit/5be49a25ea4a1d39bd3324f664dd34aafd9f529a) 2026-11-13 [AAP-99520] Fix: Insights project sync failing to copy playbooks to job execution (#16793)
- [`89e2163cfc10`](https://github.com/ansible/awx/commit/89e2163cfc10100fe77810e895e3ca2051691822) 2026-11-16 [AAP-96820] Make job adoption testable and cover its failure scenarios (#16728)
- [`7de482b075ef`](https://github.com/ansible/awx/commit/7de482b075ef78add0f49b04b26f24bf0fd5a14b) 2026-11-16 Bump sqlparse to 0.6.1 (#16798)

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

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:db7b4c9b3bd225e6d28c4b210f15c3d4d7799ffb0ab55dc352b5b0b46724a8ab` | `ghcr.io/ansible/awx:devel@sha256:5201477a711d3623fb982d1fcaff3e2f010b9cebee79ac835db08cf8d37d8851` | development tag; stable versions are not used |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | `ghcr.io/ansible/jewel:latest@sha256:b6ea83136b2f92b2ea7b583099c5c9f38a95c4905f487ffe0b18daec3075da8b` | development tag; stable versions are not used |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake).

Image versions are calver `YYYY.MM.DD` (zero-padded month and day, UTC).
Another cut the same day uses `YYYY.MM.DD-N`, and N starts at 1.

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v2026.11.16` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v2026.11.16` | upstream moved: `jewel` |
| `awx` | — | upstream moved, but `components.awx.build` is false — record the digest, do not cut an awx image |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Set `published.<component>.version` to the UTC calver only for tracks
   whose triggers moved. The first cut that day is `YYYY.MM.DD`. A later
   cut the same day is `2026.11.16-1`, `2026.11.16-2`, and so on.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.11.16 \
  --out release/notes/platform-ui-v2026.11.16.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component image is published, `release-images` dispatches
`images-released`. The operator repo pins that tag and digest and cuts
`vYYYY.MM.DD`. Do not open a second pin pull request for the same image.
See `release/AGENTS.md` and `docs/awx-image.md`.

