# platform-ui 2026.11.09

Independent component release. Git tag: `platform-ui-v2026.11.09`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:2026.11.09`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `8b64849d386e via devel` | `6ebe395827b2 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/8b64849d386e41bfbe1c3ce4d7d2722092cc1039...6ebe395827b2a20594233d23333613ff2ef6172c) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

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

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `platform-ui` `2026.11.09` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins ansible-ui to the latest devel tip. Includes security/dependency updates (DOMPurify, js-yaml, UI runtime packages), test coverage improvements across common/analytics/access/hub, UI fixes (fallback titles, credential sibling links, numeric authenticator fields, schedule survey loading), and various CI/test stabilizations. No known issues. Upstream commits serve as the changelog.

