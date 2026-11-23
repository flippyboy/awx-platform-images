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
| awx | `7de482b075ef via devel` | `f323b9ae61e5 via devel` | [compare](https://github.com/ansible/awx/compare/7de482b075ef78add0f49b04b26f24bf0fd5a14b...f323b9ae61e5ae4237355bd4b584d52ac55cfdd6) |
| jewel | `a89ef1467cfa via devel` | `0438448e3787 via devel` | [compare](https://github.com/ansible/jewel/compare/a89ef1467cfa8f0e9c5ac931298f10a0695380fa...0438448e3787ca26ae31a16ebd527f1b2ef152e8) |
| ansible-ui | `4552df6e2688 via devel` | `ba68849e3337 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/4552df6e268871c1ab37d9a60c7ddab4a19113cc...ba68849e33371727efc6099231c0644248f0efc1) |

**3** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

`7de482b075ef` → `f323b9ae61e5` — 6 commits. [compare](https://github.com/ansible/awx/compare/7de482b075ef78add0f49b04b26f24bf0fd5a14b...f323b9ae61e5ae4237355bd4b584d52ac55cfdd6)

- [`3b360cd1ad38`](https://github.com/ansible/awx/commit/3b360cd1ad38d071e2bcfdd6e6d84a4ec67ad098) 2026-11-16 chore: remove release staging and publishing workflows (#16803)
- [`b9e526b8ae57`](https://github.com/ansible/awx/commit/b9e526b8ae578b68cc22cc38e413cb1e881e79cc) 2026-11-16 [AAP-99525]fix: skip unconditional local sync for Insights projects (#16797)
- [`8a6af80c3dc1`](https://github.com/ansible/awx/commit/8a6af80c3dc1415dd919b16a769ce203addbc5e8) 2026-11-17 fix: update pyasn1 to 0.6.4 (#16578)
- [`fa68c7838d3e`](https://github.com/ansible/awx/commit/fa68c7838d3e144cfa812c10fbef987f4b779e8b) 2026-11-19 Add galaxy_update_on_launch project setting (#16737)
- [`d2762782fedb`](https://github.com/ansible/awx/commit/d2762782fedb4bc5f30153d52629218a408ff7d3) 2026-11-20 Bump djangorestframework to 3.18.2 (#16808)
- [`f323b9ae61e5`](https://github.com/ansible/awx/commit/f323b9ae61e5ae4237355bd4b584d52ac55cfdd6) 2026-11-20 Fix SonarCloud PR checkout to match CI's merge commit (#16810)

### `jewel` (`devel`)

`a89ef1467cfa` → `0438448e3787` — 6 commits. [compare](https://github.com/ansible/jewel/compare/a89ef1467cfa8f0e9c5ac931298f10a0695380fa...0438448e3787ca26ae31a16ebd527f1b2ef152e8)

- [`cf64664bb59c`](https://github.com/ansible/jewel/commit/cf64664bb59ccae4dfb4cbf9cc85faa0817a4d1b) 2026-11-18 AAP-91965 Add the jewel caller workflow for approval label auth (#347)
- [`b368c6a3b76a`](https://github.com/ansible/jewel/commit/b368c6a3b76ad5c90681f8309fca4aab39bca5b8) 2026-11-21 AAP-102564 Apply local DAB branch dependency changes in tox and dev environment (#352)
- [`47371535a10f`](https://github.com/ansible/jewel/commit/47371535a10fd4527c0bdfcb937e82544b989e1e) 2026-11-21 AAP-77767 Make xds information hidden from requests to envoy (#350)
- [`824a54bcf342`](https://github.com/ansible/jewel/commit/824a54bcf3420099c631581026c9d0f31d370d2e) 2026-11-23 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 455e3cc (#358)
- [`61ac9c95cf41`](https://github.com/ansible/jewel/commit/61ac9c95cf41df4ea5e50d525696b02805e8c9a2) 2026-11-23 [AAP-86435] Add API contract CI workflows (#353)
- [`0438448e3787`](https://github.com/ansible/jewel/commit/0438448e3787ca26ae31a16ebd527f1b2ef152e8) 2026-11-23 AAP-77767 Add opt-in API endpoint hardening controls, deprecate some ping fields (#356)

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

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:5201477a711d3623fb982d1fcaff3e2f010b9cebee79ac835db08cf8d37d8851` | `ghcr.io/ansible/awx:devel@sha256:2f81c5e63dd291e92166ce831efc0ead567dd042313343dac70e646abe47dbc6` | development tag; stable versions are not used |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:b6ea83136b2f92b2ea7b583099c5c9f38a95c4905f487ffe0b18daec3075da8b` | `ghcr.io/ansible/jewel:latest@sha256:e4edb0dd45e1131515691be2db694cdf91c470cde48d0c3ca2b5d496da13b0d2` | development tag; stable versions are not used |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake).

Image versions are calver `YYYY.MM.DD` (zero-padded month and day, UTC).
Another cut the same day uses `YYYY.MM.DD-N`, and N starts at 1.

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v2026.11.23` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v2026.11.23` | upstream moved: `jewel` |
| `awx` | — | upstream moved, but `components.awx.build` is false — record the digest, do not cut an awx image |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Set `published.<component>.version` to the UTC calver only for tracks
   whose triggers moved. The first cut that day is `YYYY.MM.DD`. A later
   cut the same day is `2026.11.23-1`, `2026.11.23-2`, and so on.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.11.23 \
  --out release/notes/platform-ui-v2026.11.23.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component image is published, `release-images` dispatches
`images-released`. The operator repo pins that tag and digest and cuts
`vYYYY.MM.DD`. Do not open a second pin pull request for the same image.
See `release/AGENTS.md` and `docs/awx-image.md`.

