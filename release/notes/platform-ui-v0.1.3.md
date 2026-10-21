# platform-ui 0.1.3

Independent component release. Git tag: `platform-ui-v0.1.3`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:0.1.3`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `4c3403d95196 via devel` | `78bde81bc413 via devel` | [compare](https://github.com/ansible/ansible-ui/compare/4c3403d951965d7d0527926f564a122588ef9ece...78bde81bc413d092b60052b336aee06eb60e3d3c) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `ansible-ui` (`devel`)

`4c3403d95196` → `78bde81bc413` — 62 commits. [compare](https://github.com/ansible/ansible-ui/compare/4c3403d951965d7d0527926f564a122588ef9ece...78bde81bc413d092b60052b336aee06eb60e3d3c)

- [`43511b0941e1`](https://github.com/ansible/ansible-ui/commit/43511b0941e119c564a50bc7118c776494640802) 2026-09-29 Apply OPTIONS normalize before client-side pattern validation (#3668)
- [`59952921771c`](https://github.com/ansible/ansible-ui/commit/59952921771c43bcf1746c5edc67549100f0cb03) 2026-09-29 fix(data-editor): keep YAML parse errors visible after blur (AAP-93178) (#3670)
- [`351242745b55`](https://github.com/ansible/ansible-ui/commit/351242745b55560cb852e0de2d0404d1a82a4957) 2026-09-30 fix(e2e): wait for Controller org sync only in Organization helper (#3681)
- [`8b2817af69f5`](https://github.com/ansible/ansible-ui/commit/8b2817af69f5e99ee55ffffab694f7b89531470b) 2026-10-01 fix(awx): sync job status links for inventory and project resources  (#3667)
- [`100227d81df8`](https://github.com/ansible/ansible-ui/commit/100227d81df84ef61c5e4d89687c982b802a7330) 2026-10-01 Check for signed commits on PR (#3664)
- [`b38935baed45`](https://github.com/ansible/ansible-ui/commit/b38935baed450481b0305d999eb13830c759d91f) 2026-10-01 Fix RevertAllDialog vitest focus-trap (follow-up to #3648) (#3688)
- [`79e4ceb86c55`](https://github.com/ansible/ansible-ui/commit/79e4ceb86c556daf07c5ffb34fcb62b2c47b19c3) 2026-10-01 fix(AAP-94066): harden PageWizard supplemental merge and launch config wait (#3640)
- [`2b72cc7c917d`](https://github.com/ansible/ansible-ui/commit/2b72cc7c917dd2aefc31a1fed61f4b3bc839b572) 2026-10-01 Use js-yaml for RequestError details (#3637)
- [`3e0ec798484e`](https://github.com/ansible/ansible-ui/commit/3e0ec798484ec700f7baccd2a5d5a3b4beeb09f8) 2026-10-01 fix: support Gateway float settings type (AAP-61719) (#3593)
- [`d1d5f1d536ab`](https://github.com/ansible/ansible-ui/commit/d1d5f1d536aba42e247532c77134f97b236c6eb0) 2026-10-01 feat: consume JSON sub-key validation patterns in UI forms (#3602)
- [`18e2cc0212b5`](https://github.com/ansible/ansible-ui/commit/18e2cc0212b59c0ba7949953a02db8948dc18f8e) 2026-10-01 Replace type-fest with local utility types (#3638)
- [`9ec99fe76d56`](https://github.com/ansible/ansible-ui/commit/9ec99fe76d560385f2c8dadd50d503fc9f392a37) 2026-10-02 [ANSTRAT-1976] Automation Dashboard Gamification UI (#3694)
- [`e8aed44768fb`](https://github.com/ansible/ansible-ui/commit/e8aed44768fb1ee40a32462a008cca00ce9f98b3) 2026-10-02 fix(test): migrate unit tests from fireEvent to userEvent (#3628)
- [`9ccc3ff902a4`](https://github.com/ansible/ansible-ui/commit/9ccc3ff902a43e78f91710f9bf3614d4483b5014) 2026-10-02 fix(e2e): restore org link on manage-roles and stabilize host bulk delete (#3682)
- [`f5876d59841b`](https://github.com/ansible/ansible-ui/commit/f5876d59841b2ec37b771e0dce57d95efc6d38a4) 2026-10-02 fix(inventories): support labels on constructed inventories (#3573)
- [`8651d9537708`](https://github.com/ansible/ansible-ui/commit/8651d9537708923684306b5e9a782ac03e46af43) 2026-10-02 [AAP-95233] Fix Job Activity chart clipping current day (#3693)
- [`3f22161a76ce`](https://github.com/ansible/ansible-ui/commit/3f22161a76cee8946f3d0b3915c23abc89bc2c08) 2026-10-06 Use Node fs.globSync in fix-coverage-paths (#3639)
- [`96c3c269019c`](https://github.com/ansible/ansible-ui/commit/96c3c269019c190a3c48eb29751cfc94c69b15de) 2026-10-06 fix(e2e): handle unsupported host filters and RBAC state (#3700)
- [`12f4242c2f02`](https://github.com/ansible/ansible-ui/commit/12f4242c2f026d6579c841e47d77575da44c61e8) 2026-10-06 chore(deps): bump proxy-addr from 2.0.7 to 2.0.8 in /frontend/hub/insights (#3708)
- [`3ee6441768aa`](https://github.com/ansible/ansible-ui/commit/3ee6441768aa6b722598357e24578d5592b9f4c4) 2026-10-06 chore(deps-dev): bump nx from 22.7.7 to 22.7.10 (#3709)
- [`10b58572163b`](https://github.com/ansible/ansible-ui/commit/10b58572163b55946b89fe3fc32f2cc81628c38a) 2026-10-06 chore(deps-dev): bump proxy-addr from 2.0.7 to 2.0.8 (#3710)
- [`5bdc94f700fb`](https://github.com/ansible/ansible-ui/commit/5bdc94f700fbc9f3a8987c1f3234b0ed5f7b9849) 2026-10-06 chore(deps): bump source-map-js from 1.2.1 to 1.2.2 (#3711)
- [`ba1664109799`](https://github.com/ansible/ansible-ui/commit/ba1664109799503f000ef88f0b1bc9fc043b6c0e) 2026-10-06 Update copied name convention to use - instead of : for timestamp (#3616)
- [`d2099b6789c8`](https://github.com/ansible/ansible-ui/commit/d2099b6789c8f3ef6b19dba5f1100e4d21db2f4c) 2026-10-06 Add OPTIONS-driven validation to EDA forms (#3619)
- [`658aa743c0c3`](https://github.com/ansible/ansible-ui/commit/658aa743c0c3bfcf263b11dfeb2171b39c73fa4b) 2026-10-06 chore(deps): bump shell-quote from 1.10.0 to 1.12.0 in /frontend/hub/insights (#3712)
- [`56bc96c7ae61`](https://github.com/ansible/ansible-ui/commit/56bc96c7ae617e399a0bd18b0a98f7c4acb08a76) 2026-10-06 chore(deps): bump i18next-http-backend from 4.0.1 to 4.0.2 (#3714)
- [`7884de9d3fb7`](https://github.com/ansible/ansible-ui/commit/7884de9d3fb7c54a66e486243eaf846b9fcc3cbb) 2026-10-06 chore(deps-dev): bump joi from 17.13.7 to 17.13.8 in /frontend/hub/insights (#3715)
- [`266aaafcb50d`](https://github.com/ansible/ansible-ui/commit/266aaafcb50d258c8ab972dc978a9da629384d52) 2026-10-06 chore(deps): bump postcss-selector-parser from 7.1.5 to 7.1.6 in /frontend/hub/insights (#3717)
- [`0bb0bd989c8a`](https://github.com/ansible/ansible-ui/commit/0bb0bd989c8a176316b302398d16538a8d16cfee) 2026-10-07 build: add production TypeScript check scope (#3650)
- [`3b81a7a5c6dd`](https://github.com/ansible/ansible-ui/commit/3b81a7a5c6dd3c66a2d2e3e2bbfa9dc5e3cb1e03) 2026-10-07 XLAB Showing the "Your organization" badge (#3703)
- [`32056e43fe97`](https://github.com/ansible/ansible-ui/commit/32056e43fe9720756c5b0537267c75ec02420422) 2026-10-07 XLAB Leaderboard shows blank organization and template names (#3721)
- [`ed009091c50e`](https://github.com/ansible/ansible-ui/commit/ed009091c50e4f76b21e292210858714ff0a0e74) 2026-10-07 XLAB Leaderboard Empty State results in error (#3704)
- [`eba518d56dac`](https://github.com/ansible/ansible-ui/commit/eba518d56dac251985ab295fe158ff5678675c75) 2026-10-07 Add CSV download for Host Metrics filtered host lists (#3666)
- [`0808558484bc`](https://github.com/ansible/ansible-ui/commit/0808558484bc0ae47bf03e11bc9d902c4efdda8e) 2026-10-08 fix: harden framework indexed access (#3651)
- [`126679ec6403`](https://github.com/ansible/ansible-ui/commit/126679ec64037340e348adaa9aeb0857579a8010) 2026-10-08 fix(awx): restore workflow job output status decorator colors (AAP-91624) (#3729)
- [`09e86ed4fba7`](https://github.com/ansible/ansible-ui/commit/09e86ed4fba74f0f4782ffa0f5cb4ae90aea9417) 2026-10-09 Hub coverage Part 3: access, my-imports, namespaces, main & overview tests (#3731)
- [`ffa246140869`](https://github.com/ansible/ansible-ui/commit/ffa24614086999a28d9eddc3bbe07a4b5518187a) 2026-10-09 XLAB Automation Analytics Settings editable only by superusers (#3730)
- [`a2d2c9d980df`](https://github.com/ansible/ansible-ui/commit/a2d2c9d980df9bada12c29e4d1e0719746bbbda5) 2026-10-09 fix(analytics): use neutral leaderboard metric definitions (AAP-96438) (#3734)
- [`7bf5ee4734ce`](https://github.com/ansible/ansible-ui/commit/7bf5ee4734ce4a67c3680740e799ffa7ed3de88b) 2026-10-09 Wire gateway settings form to OPTIONS-driven validation (#3692)
- [`a19447783470`](https://github.com/ansible/ansible-ui/commit/a19447783470e89e22ce094b2df6c44ace49aeef) 2026-10-09 feat(platform): wire Subscription Wizard to OPTIONS validation (#3684)
- [`8ad333a1187d`](https://github.com/ansible/ansible-ui/commit/8ad333a1187dd9375e3544907c0b5ac50fc150df) 2026-10-09 feat: implement OPTIONS-driven field validation across Platform and Hub forms (#3597)
- [`644817ed3e2f`](https://github.com/ansible/ansible-ui/commit/644817ed3e2ff5c5f661f032a5a472105476c1e1) 2026-10-12 Fix CVE-2026-93749 in Hub Insights lockfile (#3720)
- [`8765ccd25b4c`](https://github.com/ansible/ansible-ui/commit/8765ccd25b4cf2e2421323e920b882d5e111fdda) 2026-10-12 fix(credentials): add null guard for become_method before 'in' operator check (#3665)
- [`6fc15743d2ee`](https://github.com/ansible/ansible-ui/commit/6fc15743d2ee4b1e31c238c6bc78cef9309fa65c) 2026-10-12 AAP-95973 XLAB Leaderboard achievement alert and refresh on new sync (#3739)
- [`c3369854a5df`](https://github.com/ansible/ansible-ui/commit/c3369854a5dfdfde656ef8cd579c508cb0a23d46) 2026-10-12 restore Top 5 projects and Top 5 users cards (#3743)
- [`4f089525f662`](https://github.com/ansible/ansible-ui/commit/4f089525f66283c1c3528ed8e2916de0014ad32d) 2026-10-12 test(awx): Part 3 coverage for administration and main (AAP-72866) (#3741)
- [`70e2ecd538d3`](https://github.com/ansible/ansible-ui/commit/70e2ecd538d310e4932f039b85a64986b106dc0b) 2026-10-12 test(hub): Part 2 coverage for collections and common (AAP-72868) (#3742)
- [`48a6073a43e2`](https://github.com/ansible/ansible-ui/commit/48a6073a43e2611969277bc6db8f4d366ea7de5d) 2026-10-13 Deprecations dashboard: read deprecation text from verbose events (#3662)
- [`6fefd9870c85`](https://github.com/ansible/ansible-ui/commit/6fefd9870c85a7b8f104fdd9adbd7aa9bbb1a2ae) 2026-10-14 AAP-97426 XLAB Dashboard-local period filter and framework date range revert (#3751)
- [`262ac92e9d29`](https://github.com/ansible/ansible-ui/commit/262ac92e9d2910cf81cea25fc2eb6e09f5268e80) 2026-10-14 Replace small root dependencies with local helpers (#3636)
- [`67c523d17ac9`](https://github.com/ansible/ansible-ui/commit/67c523d17ac96b6fa34ea007adb17614f9cb1547) 2026-10-14 Fix role name search on resource user access lists (#3749)
- [`4a6e4bae1afa`](https://github.com/ansible/ansible-ui/commit/4a6e4bae1afa8d42186d05f4794cc493fc92802f) 2026-10-14 refactor(framework): enforce async select callback depth (#3698)
- [`8535f5fd83f1`](https://github.com/ansible/ansible-ui/commit/8535f5fd83f1d5576afcdde1b29d45e97541eec3) 2026-10-14 [AAP-92776] fix: guard remaining job output links with numeric id check (#3736)
- [`72f48c7e4f8d`](https://github.com/ansible/ansible-ui/commit/72f48c7e4f8d8a68fd791ba2fb56fd480b9697f1) 2026-10-14 AAP-97425 XLAB Leaderboard dimension score from activity_levels current_user_runs (#3750)
- [`da1eaf4acbc4`](https://github.com/ansible/ansible-ui/commit/da1eaf4acbc496ec46efe7813ce7ee55486f597b) 2026-10-14 fix: finish framework indexed access cleanup (#3652)
- [`8d07b46881dd`](https://github.com/ansible/ansible-ui/commit/8d07b46881dd8b1d9f084fcca922fb94836f3f58) 2026-10-15 build: migrate lint toolchain to ESLint 9 (#3728)
- [`c65902e6c3db`](https://github.com/ansible/ansible-ui/commit/c65902e6c3dbc299f63471003a19c68f11fdc5bd) 2026-10-15 fix(platform): explain missing OAuth apps on API token form (AAP-71894) (#3690)
- [`7a0fb926bfe6`](https://github.com/ansible/ansible-ui/commit/7a0fb926bfe63fe9e9c79c420ca9011d3e55e8e4) 2026-10-15 docs: guide framework-first delivery (#3753)
- [`b78f8ba944bb`](https://github.com/ansible/ansible-ui/commit/b78f8ba944bb720921bbab2557d8b2d4d2ee8c36) 2026-10-15 docs: add AI Attribution statement to README (AAP-70438) (#3762)
- [`f80c7dced40d`](https://github.com/ansible/ansible-ui/commit/f80c7dced40d9c14c8e0759a9ab7675df95c034d) 2026-10-16 docs: align README and docs with upstream workflow (AAP-72979) (#3747)
- [`b031463f6776`](https://github.com/ansible/ansible-ui/commit/b031463f6776403761f0caa84b91098be49d30fc) 2026-10-19 test(e2e): persona switcher — Automation Analytics for normal users (#3760)
- [`78bde81bc413`](https://github.com/ansible/ansible-ui/commit/78bde81bc413d092b60052b336aee06eb60e3d3c) 2026-10-19 fix(platform): show all visible teams in org role assignment wizard and Teams tab (#3588)

## Operator handoff

1. Bump **only** `platform-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.3` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
4. Cut an operator release only when the operator itself or chart defaults need a ship.

## Notes

ansible-ui `devel` moved 62 commits past the 0.1.2 pin (`4c3403d95196` → `78bde81bc413`). This cut follows that tip. Notable: OPTIONS-driven validation improvements across forms, dashboard and leaderboard fixes, dependency bumps, and CVE remediation in Hub Insights. The commit list above is the full changelog.

