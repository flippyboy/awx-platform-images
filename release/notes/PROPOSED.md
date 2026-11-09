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
| awx | `8565291e43e1 via devel` | `d4159cab745d via devel` | [compare](https://github.com/ansible/awx/compare/8565291e43e17cd1ee5333e82e57aeb230e6574e...d4159cab745d1fa6e2247bf3cf7aae4b0546f1b3) |
| jewel | `a39b016d5bc6 via devel` | `63f7efe90075 via devel` | [compare](https://github.com/ansible/jewel/compare/a39b016d5bc6846a4d6262d4820dbcc91daf355a...63f7efe900750b0886ad6b86ee60b6a4aba3058f) |
| ansible-ui | `8b64849d386e via devel` | `6ebe395827b2 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/8b64849d386e41bfbe1c3ce4d7d2722092cc1039...6ebe395827b2a20594233d23333613ff2ef6172c) |

**3** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

`8565291e43e1` → `d4159cab745d` — 8 commits. [compare](https://github.com/ansible/awx/compare/8565291e43e17cd1ee5333e82e57aeb230e6574e...d4159cab745d1fa6e2247bf3cf7aae4b0546f1b3)

- [`ac5bfc720955`](https://github.com/ansible/awx/commit/ac5bfc720955f52dbdd95f5439ab49df25d586a6) 2026-11-03 fix: define asyncio_default_fixture_loop_scope to avoid failing in re… (#16776)
- [`a49831067591`](https://github.com/ansible/awx/commit/a498310675911e8f8f4588a09f9ccb1263e27e12) 2026-11-03 fix: update gitpython to 3.2.1 (#16769)
- [`85ad07ed6e3f`](https://github.com/ansible/awx/commit/85ad07ed6e3f2252e7f58c785268206d4b187545) 2026-11-04 fix: bump urllib3 to 2.8.0 (#16775)
- [`fe6cd9d45a7e`](https://github.com/ansible/awx/commit/fe6cd9d45a7e977e2b78c8e8e5e69cc24d7eeaaa) 2026-11-05 Fix EDITABLE_DEPENDENCIES=true make docker-compose (#16767)
- [`5054397c26b9`](https://github.com/ansible/awx/commit/5054397c26b924868063ed3f62d8d4cd359f77a4) 2026-11-09 AAP-90162 Run SQLite-backed tests on a current SQLite via sqlean.py (#16784)
- [`c02e6a751318`](https://github.com/ansible/awx/commit/c02e6a751318c04eb36da5377030bf895561cf5c) 2026-11-09 fix: make receptor work-unit reapers resilient to per-unit failures (AAP-97861) (#16774)
- [`cac2ca78cb9f`](https://github.com/ansible/awx/commit/cac2ca78cb9fd06b5750ff95ea6f80dbd86dc981) 2026-11-09 fix: tear down receptor results stream before work release (AAP-97861) (#16773)
- [`d4159cab745d`](https://github.com/ansible/awx/commit/d4159cab745d1fa6e2247bf3cf7aae4b0546f1b3) 2026-11-09 fix: centralize CI Python version in .github/python-version (#16786)

### `jewel` (`devel`)

`a39b016d5bc6` → `63f7efe90075` — 7 commits. [compare](https://github.com/ansible/jewel/compare/a39b016d5bc6846a4d6262d4820dbcc91daf355a...63f7efe900750b0886ad6b86ee60b6a4aba3058f)

- [`6cb5e8599197`](https://github.com/ansible/jewel/commit/6cb5e8599197c6186a22a7915ccf5c58c1f02733) 2026-11-02 AAP-100941 Update oauthlib to 4.0.1 (#321)
- [`661aa0534ac9`](https://github.com/ansible/jewel/commit/661aa0534ac9bb553a8ddf898491b176d0eb5c3e) 2026-11-03 [AAP-100958] Upgrade pyasn1 to 0.6.5 (#324)
- [`fc4cc3f12f74`](https://github.com/ansible/jewel/commit/fc4cc3f12f749fb46a2a1e796ef5fa8c48ecb2c3) 2026-11-04 fix(envoy): Disable X25519MLKEM768 on FIPS (#326)
- [`9705052bda17`](https://github.com/ansible/jewel/commit/9705052bda17753530ad8371c55a5a167d62dae0) 2026-11-05 [Devel] [AAP-96817] Added deprecation headers to existing deprecations (#288)
- [`7fc61e5421a3`](https://github.com/ansible/jewel/commit/7fc61e5421a3f41b4c7019bde0d00ff9f37ab021) 2026-11-06 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to fbbe116 (#330)
- [`1fa6e6c6eec5`](https://github.com/ansible/jewel/commit/1fa6e6c6eec59d9f7fe38b4c3bc1896c095c1ce3) 2026-11-09 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 0557ee8 (#333)
- [`63f7efe90075`](https://github.com/ansible/jewel/commit/63f7efe900750b0886ad6b86ee60b6a4aba3058f) 2026-11-09 Added named to org and team factory (#335)

### `ansible-ui` (`devel`)

`8b64849d386e` → `6ebe395827b2` — 21 commits. [compare](https://github.com/ansible/ansible-ui/compare/8b64849d386e41bfbe1c3ce4d7d2722092cc1039...6ebe395827b2a20594233d23333613ff2ef6172c)

- [`da34bcb7947c`](https://github.com/ansible/ansible-ui/commit/da34bcb7947caf6a87afe35404b57fce3aa73145) 2026-11-03 chore(eslint): enforce no-debugging-utils in test guardrails (#3850)
- [`dc5d224ab165`](https://github.com/ansible/ansible-ui/commit/dc5d224ab16527952a7023ecd459832a5cbd5ebc) 2026-11-03 chore(deps): update build-tools digest to 687944f (#3603)
- [`140609c8a498`](https://github.com/ansible/ansible-ui/commit/140609c8a4985ecfaf7d2de3ceab8a0fdae0af7c) 2026-11-03 chore(deps): update konflux references (#3604)
- [`373873c5b701`](https://github.com/ansible/ansible-ui/commit/373873c5b701a16086ec9b520a03ad80eaec2a48) 2026-11-03 fix(awx): use a fallback title for unknown resources (#3847)
- [`c79dab5fd86d`](https://github.com/ansible/ansible-ui/commit/c79dab5fd86d40212c0f839ff74bb8926983b760) 2026-11-04 test(common): Part 2 coverage for columns, crud, and shared UI (AAP-72870) (#3844)
- [`b04ab829f43d`](https://github.com/ansible/ansible-ui/commit/b04ab829f43d4cec93dbb18e9d34139dda80829d) 2026-11-04 AAP-70846: Increase hub administration/ and execution-environments/ coverage to 90%+ (#3839)
- [`aaa3d583cb08`](https://github.com/ansible/ansible-ui/commit/aaa3d583cb089c7c21b63f4e577e1c6e115d0ca5) 2026-11-04 fix(credentials): preserve sibling lookup links when replacing one field (#3838)
- [`508678660ec2`](https://github.com/ansible/ansible-ui/commit/508678660ec239e5b4e0832613617d3081e287ef) 2026-11-05 refactor(awx): split template survey validation (#3777)
- [`f10789d39088`](https://github.com/ansible/ansible-ui/commit/f10789d390886fbcf40c1a00b0e62d4ca66d54cc) 2026-11-05 [AAP-72867 ]test(eda): raise remaining directory coverage above 90% (#3855)
- [`e51e1f3d4c2d`](https://github.com/ansible/ansible-ui/commit/e51e1f3d4c2db9f34904524a758261642d1d26ee) 2026-11-05 test(platform): use userEvent in org teams add roles cache test (#3779)
- [`17f995472a1a`](https://github.com/ansible/ansible-ui/commit/17f995472a1a2c9e24a61652deedb9764a5b5010) 2026-11-05 fix(framework): allow bounded numbers to be typed incrementally (#3768)
- [`860ea3244948`](https://github.com/ansible/ansible-ui/commit/860ea32449486ded197de9b8cbbb0a79e0263ae7) 2026-11-05 test(awx): raise Vitest coverage for common (#3860)
- [`68a3df3b476b`](https://github.com/ansible/ansible-ui/commit/68a3df3b476bf28e081c221faf025a86073a90bd) 2026-11-05 fix: disable mint maker running pipeline-migration-tool (#3869)
- [`50203c221e87`](https://github.com/ansible/ansible-ui/commit/50203c221e87074784dc5e13d3e73736449b2c75) 2026-11-05 chore(deps): update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-ui-tests:0.1 docker digest to 3ec96e2 (#3545)
- [`04aef6eb0288`](https://github.com/ansible/ansible-ui/commit/04aef6eb0288bd1d855400984b353b3d0ea3a072) 2026-11-06 test(awx): raise Vitest coverage for analytics/ (AAP-72865) (#3863)
- [`eed24028a635`](https://github.com/ansible/ansible-ui/commit/eed24028a6356829dc47c46fa6a408755b3fc48c) 2026-11-06 test(awx): raise Vitest coverage for access/ (AAP-72865) (#3862)
- [`8cd40dd723c8`](https://github.com/ansible/ansible-ui/commit/8cd40dd723c8191d3a04978bd22fd4c0c4058866) 2026-11-06 [AAP-101595] Render numeric authenticator fields (#3876)
- [`bdba4e9219ec`](https://github.com/ansible/ansible-ui/commit/bdba4e9219ecd7a64002a8c837448db8bab17498) 2026-11-06 fix(awx): load survey spec in top-level schedule create wizard (AAP-64057) (#3820)
- [`cf9d5706dd81`](https://github.com/ansible/ansible-ui/commit/cf9d5706dd813930b6ea60c52fb118eb82bc67c1) 2026-11-06 Stabilize live Playwright checks (#3856)
- [`0df6a684d9f5`](https://github.com/ansible/ansible-ui/commit/0df6a684d9f503d8879a97e572eb0c6220c3990f) 2026-11-06 chore(deps): update UI runtime packages (#3783)
- [`6ebe395827b2`](https://github.com/ansible/ansible-ui/commit/6ebe395827b2a20594233d23333613ff2ef6172c) 2026-11-09 chore(deps): update DOMPurify and js-yaml (#3782)

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:db7b4c9b3bd225e6d28c4b210f15c3d4d7799ffb0ab55dc352b5b0b46724a8ab` | `ghcr.io/ansible/awx:devel@sha256:db7b4c9b3bd225e6d28c4b210f15c3d4d7799ffb0ab55dc352b5b0b46724a8ab` | (unchanged) |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | `ghcr.io/ansible/jewel:latest@sha256:fed2caa141fc1a158edb180ae2c8c08407c56467179bbc6bdb6c5c8718d0311d` | (unchanged) |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake).

Image versions are calver `YYYY.MM.DD` (zero-padded month and day, UTC).
Another cut the same day uses `YYYY.MM.DD-N`, and N starts at 1.

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v2026.11.09` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v2026.11.09` | upstream moved: `jewel` |
| `awx` | — | upstream moved, but `components.awx.build` is false — record the digest, do not cut an awx image |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Set `published.<component>.version` to the UTC calver only for tracks
   whose triggers moved. The first cut that day is `YYYY.MM.DD`. A later
   cut the same day is `2026.11.09-1`, `2026.11.09-2`, and so on.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.11.09 \
  --out release/notes/platform-ui-v2026.11.09.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component image is published, `release-images` dispatches
`images-released`. The operator repo pins that tag and digest and cuts
`vYYYY.MM.DD`. Do not open a second pin pull request for the same image.
See `release/AGENTS.md` and `docs/awx-image.md`.

