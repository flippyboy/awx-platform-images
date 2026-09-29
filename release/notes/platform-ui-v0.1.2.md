# platform-ui 0.1.2

Independent component release. Git tag: `platform-ui-v0.1.2`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:0.1.2`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `6fe43c634d1a via devel` | `4c3403d95196 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/6fe43c634d1affa5e82ef0529f4412869c8d8fca...4c3403d951965d7d0527926f564a122588ef9ece) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `ansible-ui` (`devel`)

`6fe43c634d1a` → `4c3403d95196` — 89 commits. [compare](https://github.com/ansible/ansible-ui/compare/6fe43c634d1affa5e82ef0529f4412869c8d8fca...4c3403d951965d7d0527926f564a122588ef9ece)

- [`aca81eeb6ca9`](https://github.com/ansible/ansible-ui/commit/aca81eeb6ca9f6a16171253e766374326afb03a8) 2026-08-26 [AAP-72862] test(framework): coverage Part 3 — components, dashboard & remaining (#3498)
- [`d6756bedddb1`](https://github.com/ansible/ansible-ui/commit/d6756bedddb18054a929d79921dbaff251a66e62) 2026-08-26 fix(deps): override brace-expansion to 5.0.9 for CVE-2026-14257 (#3506)
- [`0095976dec7e`](https://github.com/ansible/ansible-ui/commit/0095976dec7ecc5e9857e919ba928b368f1b62dd) 2026-08-26 Add public AI disclosure policies and remove committed agent hooks (#3502)
- [`2af48c23281d`](https://github.com/ansible/ansible-ui/commit/2af48c23281d84a5d07b7c98436414dde0ad1109) 2026-08-26 fix(deps): override brace-expansion for CVE-2026-69152 (#3500)
- [`57bc41ce832e`](https://github.com/ansible/ansible-ui/commit/57bc41ce832e1f67c5d2d329ab15a1c3769d67de) 2026-08-27 Shrink CLAUDE.md to a skill trigger table (#3503)
- [`02b5ab6cfce9`](https://github.com/ansible/ansible-ui/commit/02b5ab6cfce977a9d3e5f0eea23b62b2b918f026) 2026-08-27 fix(deps): pin @playwright/test to 1.57.0 to match CI runner image (#3512)
- [`a86263b97334`](https://github.com/ansible/ansible-ui/commit/a86263b973348e84800effa5a15776950bebafc5) 2026-08-31 Show authenticator options on detail page (#3517)
- [`7c3ef76286ec`](https://github.com/ansible/ansible-ui/commit/7c3ef76286ec2aa8fd470ea42e09db6975d8bb27) 2026-08-31 chore: Standard SECURITY.md (#3518)
- [`a546a375ee95`](https://github.com/ansible/ansible-ui/commit/a546a375ee95db36b487ee8eadd46d40588816ce) 2026-08-31 Stabilize inventory util timeout (#3508)
- [`2c605554c2b4`](https://github.com/ansible/ansible-ui/commit/2c605554c2b4e1819450c55de2f74cc87835ffe2) 2026-08-31 fix(e2e): prevent 3-minute timeout in credential Team/User Access tests (#3521)
- [`8c17dff06c5c`](https://github.com/ansible/ansible-ui/commit/8c17dff06c5c4804c6a9dc57907a6f7ec8bb1c42) 2026-09-01 fix(awx): fix workflow node prompt string fields not clearing when saved (#3510)
- [`8dd795793f42`](https://github.com/ansible/ansible-ui/commit/8dd795793f426d83353cb19cb241359dcef19b1f) 2026-09-02 fix(e2e): select Default org without depending on its description (#3532)
- [`34447f618f75`](https://github.com/ansible/ansible-ui/commit/34447f618f7501513a43629e37cc69436d7c2433) 2026-09-02 fix(AAP-90404): paste into Monaco via clipboard to avoid JSON corruption (#3528)
- [`bb976594d2ff`](https://github.com/ansible/ansible-ui/commit/bb976594d2ffea77ad22d22fafaf9046a5bd7c36) 2026-09-02 Remove redundant SWRConfig wrappers from tests (#3534)
- [`f2b1925c19b1`](https://github.com/ansible/ansible-ui/commit/f2b1925c19b1cd9c3ef69291a19bcb623ff34508) 2026-09-02 chore(deps-dev): bump the non-major-dev group across 1 directory with 13 updates (#3531)
- [`cfd21384cd04`](https://github.com/ansible/ansible-ui/commit/cfd21384cd04f0cc309361cead1d8f15734065eb) 2026-09-03 Stabilize live inventory and credential-type Playwright assertions (#3522)
- [`b4d356cd357f`](https://github.com/ansible/ansible-ui/commit/b4d356cd357fedf09e280f8d04fee188463791a4) 2026-09-03 Improve wait before asserting saved changes (#3527)
- [`b5dfc6fcfa4e`](https://github.com/ansible/ansible-ui/commit/b5dfc6fcfa4ed64ae198f705491cfb1d1401f914) 2026-09-03 Add evidence-backed PR-review checks to review skills (#3513)
- [`2eec5f59a2be`](https://github.com/ansible/ansible-ui/commit/2eec5f59a2bef83e87acfc3ced0a6acea425fa32) 2026-09-09 Add React/TS, a11y, and Playwright guidance to skills (#3514)
- [`2aded90b9b68`](https://github.com/ansible/ansible-ui/commit/2aded90b9b68ff1bbfd5fa6ed1fe155e5831aac4) 2026-09-09 Add knip as an advisory unused-code report on pull requests (#3507)
- [`8261a7a2de5b`](https://github.com/ansible/ansible-ui/commit/8261a7a2de5b22f5572d9b2cd4f7e41307281132) 2026-09-09 fix(awx): show workflow approval description on details page (AAP-87838) (#3548)
- [`1a303f8437ad`](https://github.com/ansible/ansible-ui/commit/1a303f8437ad4eb424ce10e4ef96d3625847cbe4) 2026-09-09 Show empty-string extra vars on job Details (AAP-85950) (#3546)
- [`d1ca38618f3c`](https://github.com/ansible/ansible-ui/commit/d1ca38618f3ce57e9186bcb782ed5bc8d91cee82) 2026-09-09 chore(framework): remove unused modules (#3542)
- [`5c6af38a23f7`](https://github.com/ansible/ansible-ui/commit/5c6af38a23f780174aaaa364aafcb7ac33a2dbfa) 2026-09-09 Add instructions for signing commits (#3557)
- [`fc25842a224d`](https://github.com/ansible/ansible-ui/commit/fc25842a224dcda0e4cac0f4ee775dede41958dc) 2026-09-09 fix(hub): render GFM markdown in execution environment READMEs (#3496)
- [`eaae0da43199`](https://github.com/ansible/ansible-ui/commit/eaae0da4319993473fc7c861fc61c72ae8fbb8c3) 2026-09-10 chore(deps): bump uuid from 11.0.5 to 14.0.2 (#3427)
- [`7fbc0837eb0c`](https://github.com/ansible/ansible-ui/commit/7fbc0837eb0cab7f36da6e57473aaff8a760fe0c) 2026-09-10 chore(deps): bump react-router and react-router-dom (#3457)
- [`af5ae4c20bcd`](https://github.com/ansible/ansible-ui/commit/af5ae4c20bcd33a265b469719ea6cf7ad9053372) 2026-09-10 chore(deps-dev): bump sanitize-html from 2.17.6 to 2.17.7 in /frontend/hub/insights (#3530)
- [`2caceb1fa044`](https://github.com/ansible/ansible-ui/commit/2caceb1fa044ed0daa251955a8fff92487a7f9e0) 2026-09-10 chore(deps-dev): bump browserslist from 4.28.1 to 4.28.8 in /frontend/hub/insights (#3536)
- [`5c46c493deaf`](https://github.com/ansible/ansible-ui/commit/5c46c493deaf7785bed305f501c3074e7b081e00) 2026-09-10 chore(deps): bump js-yaml from 4.3.1 to 4.3.2 in /frontend/hub/insights (#3553)
- [`c674d0f0a8d9`](https://github.com/ansible/ansible-ui/commit/c674d0f0a8d9a2bcb9348fc569fe7e91edce63e8) 2026-09-10 chore(deps-dev): bump svgo from 3.3.4 to 3.3.5 in /frontend/hub/insights (#3554)
- [`65a2f3f4dfe9`](https://github.com/ansible/ansible-ui/commit/65a2f3f4dfe973dbc8695947f08b846287f1c959) 2026-09-10 chore(deps-dev): bump joi from 17.13.3 to 17.13.7 in /frontend/hub/insights (#3556)
- [`54bd0a785676`](https://github.com/ansible/ansible-ui/commit/54bd0a785676777ac2a4228df90d84adbf1621a0) 2026-09-10 chore(deps): bump postcss-selector-parser from 7.1.1 to 7.1.5 in /frontend/hub/insights (#3529)
- [`e339d860a86d`](https://github.com/ansible/ansible-ui/commit/e339d860a86df8c6b795cf6c2c1641fb3024d118) 2026-09-10 Fix subscription config refresh race (#3549)
- [`620fc5238e61`](https://github.com/ansible/ansible-ui/commit/620fc5238e6110b2eb71706f29562b281ccdf258) 2026-09-10 [AAP-84126] refactor(deps): replace debounce packages (#3544)
- [`9e320a7995b6`](https://github.com/ansible/ansible-ui/commit/9e320a7995b6d4e802a7a815c9d9b3d0da151edf) 2026-09-11 [AAP-92380] Stabilize workflow visualizer save assertion (#3561)
- [`f67dfd521e87`](https://github.com/ansible/ansible-ui/commit/f67dfd521e87fc79542c6892ec013ca256fd9a0f) 2026-09-11 feat(framework): OPTIONS-driven validation in PageForm & PageWizard (#3543)
- [`a3cb1a4c6af6`](https://github.com/ansible/ansible-ui/commit/a3cb1a4c6af68e304a2c6dd777e2fab2c771f268) 2026-09-11 fix: exclude large fields from jobs list request (#3551)
- [`24a5f8675d8c`](https://github.com/ansible/ansible-ui/commit/24a5f8675d8ca393f22cee7bf77009c8bc4c5830) 2026-09-14 fix(e2e): stabilize Monaco editor fill for credential types CRUD (#3559)
- [`d576c764b3e9`](https://github.com/ansible/ansible-ui/commit/d576c764b3e9200caca667027023c5226578d98e) 2026-09-14 fix(e2e): fix Source Control Update job test timeout (#3523)
- [`02a000ea58f9`](https://github.com/ansible/ansible-ui/commit/02a000ea58f930d8668d7cce80ae6bc508e819d8) 2026-09-14 fix(e2e): repair rulebook activation auto-restart table filter (#3558)
- [`500334f82355`](https://github.com/ansible/ansible-ui/commit/500334f8235547727e26371e5a7e6df99012c421) 2026-09-15 chore(deps): update konflux references (#3495)
- [`a8947ff45981`](https://github.com/ansible/ansible-ui/commit/a8947ff45981e24bd86dfd502dbbdbe5e0f8391f) 2026-09-15 chore(deps): update build-tools digest to 5307281 (#3302)
- [`6aa2478b4910`](https://github.com/ansible/ansible-ui/commit/6aa2478b49106f36d040b75d64f5d0814c299f29) 2026-09-15 docs: add dynamic string i18n review check (#3580)
- [`c70361ce63d9`](https://github.com/ansible/ansible-ui/commit/c70361ce63d95fcacfd12751b23c44fcceb646fd) 2026-09-15 fix(survey): render question names containing colons (#3577)
- [`3bb540266b24`](https://github.com/ansible/ansible-ui/commit/3bb540266b241c12c532d942a47d0a2770a9e912) 2026-09-16 Use PlatformPageForm with errorAdapter across all forms (#3587)
- [`34aca6d8a798`](https://github.com/ansible/ansible-ui/commit/34aca6d8a798e86e59487aa915a7c571dd6d7c39) 2026-09-16 [AAP-84126] fix(deps): drop unused leftover packages (#3511)
- [`025d0b645af7`](https://github.com/ansible/ansible-ui/commit/025d0b645af769e24125d4ddebc1086716dfb977) 2026-09-17 Replace uuid dependency with native function (#3584)
- [`b05dc6541e0d`](https://github.com/ansible/ansible-ui/commit/b05dc6541e0d3ff6f567b4cdee43fb21283e96a2) 2026-09-17 test(playwright): wait for organization propagation (#3571)
- [`c3e5007b5201`](https://github.com/ansible/ansible-ui/commit/c3e5007b52014ca3f7daae8b78b5f83b1677adda) 2026-09-17 test(e2e): avoid Monaco typing for constructed inventory vars (#3581)
- [`6ec449d1c224`](https://github.com/ansible/ansible-ui/commit/6ec449d1c224ebc36e13c6e4e094be16eb07b7f8) 2026-09-17 fix(deps): add npm override for fflate to remediate CVE-2026-45820 (#3585)
- [`34eaa7373a40`](https://github.com/ansible/ansible-ui/commit/34eaa7373a401c6558fc6ee9c94e3578e7069726) 2026-09-17 chore(node): move CI and engines to Node 24 LTS (#3583)
- [`f79a0e292cf7`](https://github.com/ansible/ansible-ui/commit/f79a0e292cf74e5ad443d23572667437e057a711) 2026-09-17 [AAP-91925] Fix E2E failures in Template and Project Flow (#3599)
- [`532950320056`](https://github.com/ansible/ansible-ui/commit/5329503200569ad7ec278cc5119c2df0dd4d5ebc) 2026-09-17 test(awx): wait for deprecations dashboard search filter (#3596)
- [`69452de74df7`](https://github.com/ansible/ansible-ui/commit/69452de74df7aee2711ce04b45ee4113ea3c53e8) 2026-09-17 chore(awx): remove unused hooks, components, and interfaces (#3563)
- [`757ea2941d0b`](https://github.com/ansible/ansible-ui/commit/757ea2941d0b192f0b82e2817096fc0e71b7fb64) 2026-09-17 chore(eda): remove unused interfaces and components (#3564)
- [`8a7d32b99c27`](https://github.com/ansible/ansible-ui/commit/8a7d32b99c274c518ed848efef452af4f3e530c5) 2026-09-17 chore(platform): remove unused hooks, interfaces, and components (#3566)
- [`ba874fd8e516`](https://github.com/ansible/ansible-ui/commit/ba874fd8e516ce83c41e1e84ceb627de75cb4cba) 2026-09-17 fix(e2e): stabilize EE access and inventory host/group bulk-delete specs (#3572)
- [`17028b4c026f`](https://github.com/ansible/ansible-ui/commit/17028b4c026f91bbd268cb0e96dc5be0a9491bf7) 2026-09-18 [AAP-78704] Add Options Driven Validation to AWX Forms (#3562)
- [`ac8ef5379d1b`](https://github.com/ansible/ansible-ui/commit/ac8ef5379d1b667c000c2bc4341a214785bad757) 2026-09-18 [AAPRFE-126] Fix FR translations (#3525)
- [`5a6f1d25882c`](https://github.com/ansible/ansible-ui/commit/5a6f1d25882c5e30c7fd538ac9a03383f3f7b0c1) 2026-09-21 fix(e2e): stabilize EDA credential tabs and event persistence setup (#3576)
- [`06d633a12938`](https://github.com/ansible/ansible-ui/commit/06d633a12938e568212c6e88b036022f22e125e1) 2026-09-22 Add advisory ESLint readability guardrails (#3533)
- [`e99747fea390`](https://github.com/ansible/ansible-ui/commit/e99747fea3908d91eb5c84276f7e98fc4ee6ea10) 2026-09-22 [AAP-82758] Keep Add step and link sequential in Workflow Visualizer (#3586)
- [`ca47b5d35394`](https://github.com/ansible/ansible-ui/commit/ca47b5d3539463a2b8a33e635206aa40da638e4a) 2026-09-22 chore(types): pilot side-effect import checks (#3612)
- [`e86e8d8d6be9`](https://github.com/ansible/ansible-ui/commit/e86e8d8d6be914017749cdc71991412f6679f9a9) 2026-09-22 chore(knip): ignore generated and build-only files (#3609)
- [`c09fd8b4bc13`](https://github.com/ansible/ansible-ui/commit/c09fd8b4bc136f079bd6999f281414b43b16b834) 2026-09-22 docs: require MCP consultation for UI changes (#3579)
- [`c6b2e596523f`](https://github.com/ansible/ansible-ui/commit/c6b2e596523f6dd5a35f0dc79c14b5b43dfa7ab3) 2026-09-22 chore(hub,common): remove unused components and hooks (#3565)
- [`9eb54f0d6cb1`](https://github.com/ansible/ansible-ui/commit/9eb54f0d6cb1ee29e8756e7fcd366e89ae693a78) 2026-09-22 update @ansible/ansible-ai-connect-chatbot to version 0.1.17 (#3621)
- [`066ea8de3006`](https://github.com/ansible/ansible-ui/commit/066ea8de300697a13a2c1d360ea05c9a84cd1996) 2026-09-22 Enable unused local checks in TypeScript (#3569)
- [`74c6daf94cc8`](https://github.com/ansible/ansible-ui/commit/74c6daf94cc860159abba7dad2e638d553674fc7) 2026-09-22 fix(ci): scope codecov/project status to unit-tests flag (#3624)
- [`69466bb15fad`](https://github.com/ansible/ansible-ui/commit/69466bb15fad8cf3a953f8c39f5e4d3fe9f13cbe) 2026-09-22 fix(schedules): preserve Z suffix on UNTIL when splitting rrule components (#3472)
- [`c5b2efeed021`](https://github.com/ansible/ansible-ui/commit/c5b2efeed021fb068d628a3c5681b72e2e6f7aec) 2026-09-22 fix(roles): add change activation permission (#3538)
- [`5ff0f77f6262`](https://github.com/ansible/ansible-ui/commit/5ff0f77f6262e988abf025078b14c476474afaa6) 2026-09-22 fix(job-output): show status counts in legends (#3539)
- [`35e87ee2a86f`](https://github.com/ansible/ansible-ui/commit/35e87ee2a86f338bc3d74aeadbcc5cc46a3134ee) 2026-09-22 fix(e2e): stabilize live run failures and flaky specs (#3615)
- [`364c913490df`](https://github.com/ansible/ansible-ui/commit/364c913490df0365c497c415fc4a44d28cc1391f) 2026-09-22 [AAP-82489] fix: show detailed error message on template launch failure (#3617)
- [`6318aa9a220d`](https://github.com/ansible/ansible-ui/commit/6318aa9a220d66017ba6670f32b9389ab44765ce) 2026-09-22 fix(framework): resolve Safari WebKit table rendering and height collapse in Scrollable (#3541)
- [`1833c831492b`](https://github.com/ansible/ansible-ui/commit/1833c831492b33d05e1faae14b8abc77230a68f1) 2026-09-23 chore(platform): remove unused content type metadata hooks (#3608)
- [`a067177126bf`](https://github.com/ansible/ansible-ui/commit/a067177126bf20d007a7c5e392bce2abaf6cfebd) 2026-09-23 chore: migrate ESLint configs to flat config (#3611)
- [`f1294f92427b`](https://github.com/ansible/ansible-ui/commit/f1294f92427ba9ba43f78312062cbe37f0cc100a) 2026-09-23 Restore legacy cypress e2e workflow (#3642)
- [`438bae84b396`](https://github.com/ansible/ansible-ui/commit/438bae84b396ec49a27c693e62e9529778d12069) 2026-09-23 Platform coverage Part 2: main, routes & resource tests (#3625)
- [`c93c4e7782fb`](https://github.com/ansible/ansible-ui/commit/c93c4e7782fba8bffa455629d544f0141df5b7c4) 2026-09-24 [AAP-91941] Rebuild translation catalogs (#3641)
- [`f4e250b7ea2c`](https://github.com/ansible/ansible-ui/commit/f4e250b7ea2c617f2538ab2142196ec70877617c) 2026-09-24 fix(automation-dashboard): exclude system jobs from report data (AAP-92027) (#3589)
- [`6fad519aa1a6`](https://github.com/ansible/ansible-ui/commit/6fad519aa1a61137106040f3687643d575ee7794) 2026-09-24 Document maintainer review patterns in agent skills (#3649)
- [`7678e3a1a21a`](https://github.com/ansible/ansible-ui/commit/7678e3a1a21ad6eab2b2094709e91b5679fc281a) 2026-09-25 ci: enforce Knip unused-code checks
- [`d38d1517dfe7`](https://github.com/ansible/ansible-ui/commit/d38d1517dfe7b98b646915b3937610033731dd83) 2026-09-25 [AAP-71569] Prefill workflow node prompts from the job template (#3620)
- [`36fc16aee837`](https://github.com/ansible/ansible-ui/commit/36fc16aee837c64f628da3c6d645691c22910a7d) 2026-09-25 chore(test): add advisory Vitest and Testing Library ESLint guardrails (#3626)
- [`3eb11da7d0bc`](https://github.com/ansible/ansible-ui/commit/3eb11da7d0bc483181f82dffc55941087cd14a7c) 2026-09-25 [READY] Make host name clickable in the job output host event modal (#3622)
- [`77a3a24b042f`](https://github.com/ansible/ansible-ui/commit/77a3a24b042f96f4c362129f476997a1d0a676e0) 2026-09-28 Platform coverage Part 3: overview, settings & remaining (#3648)
- [`4c3403d95196`](https://github.com/ansible/ansible-ui/commit/4c3403d951965d7d0527926f564a122588ef9ece) 2026-09-28 fix(data-editor): prevent YAML block-scalar growth loop on invalid input (#3600)

## Operator handoff

1. Bump **only** `platform-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.2` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
4. Cut an operator release only when the operator itself or chart defaults need a ship.

## Notes

ansible-ui `devel` moved 89 commits past the 0.1.1 pin (`6fe43c634d1a` →
`4c3403d95196`). This cut follows that tip. Stable tags such as `v2.4.313`
stay off the pin.

The image Dockerfile no longer copies `ansible-ui/webpack`. That directory
is gone on this pin; the platform build is Vite.

Notable changes in that range: brace-expansion overrides for CVE-2026-14257
and CVE-2026-69152, workflow-node prompts prefilled from the job template,
authenticator options on the detail page, rebuilt translation catalogs, and
a data-editor fix that stopped YAML block scalars from growing on invalid
input. The commit list above is the full changelog.

