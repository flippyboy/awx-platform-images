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
| awx | `e995e5fc5f92 via devel` | `918ba2ef36e2 via devel` | [compare](https://github.com/ansible/awx/compare/e995e5fc5f925078aab296acda5acb1df39b49d0...918ba2ef36e274e8a58295849eebab572177053e) |
| jewel | `e680bd860a58 via devel` | `21a64d4febac via devel` | [compare](https://github.com/ansible/jewel/compare/e680bd860a58db23380c0b12807d31cab71856ef...21a64d4febac435fc949f106ac6a128ce73754df) |
| ansible-ui | `4c3403d95196 via devel` | `6fc15743d2ee via devel` | [compare](https://github.com/ansible/ansible-ui/compare/4c3403d951965d7d0527926f564a122588ef9ece...6fc15743d2ee4b1e31c238c6bc78cef9309fa65c) |

**3** upstream pin(s) changed.

## Upstream commits

Use this list as the release-note changelog when you cut a component.
Subjects are the upstream commit messages.

### `awx` (`devel`)

`e995e5fc5f92` → `918ba2ef36e2` — 5 commits. [compare](https://github.com/ansible/awx/compare/e995e5fc5f925078aab296acda5acb1df39b49d0...918ba2ef36e274e8a58295849eebab572177053e)

- [`3c76e236c270`](https://github.com/ansible/awx/commit/3c76e236c270b831f0f71465c3e0d7fae040c83a) 2026-09-30 [AAP-93690] Add CleanText validation and OPTIONS patterns to subscription wizard (#16671)
- [`e4a42b0399a9`](https://github.com/ansible/awx/commit/e4a42b0399a929586060a55e2fac4f8d0ec85f68) 2026-10-02 [AAP-93983] Update schema to add pattern fields for credential types (#16670)
- [`33a9eb7d15ae`](https://github.com/ansible/awx/commit/33a9eb7d15aedca7222354b68cde834480415913) 2026-10-02 Pin ruff to a compatible release (~=0.16.0) (#16694)
- [`f8314ada7292`](https://github.com/ansible/awx/commit/f8314ada72926580f2fe465c8eed7d41a726c363) 2026-10-10 [AAP-93974] perf(api): optimize non-superuser job list pagination (#16668)
- [`918ba2ef36e2`](https://github.com/ansible/awx/commit/918ba2ef36e274e8a58295849eebab572177053e) 2026-10-12 AAP-95887 Use SKIP LOCKED to prevent lock convoy on parent JT update (#16719)

### `jewel` (`devel`)

`e680bd860a58` → `21a64d4febac` — 17 commits. [compare](https://github.com/ansible/jewel/compare/e680bd860a58db23380c0b12807d31cab71856ef...21a64d4febac435fc949f106ac6a128ce73754df)

- [`c0e9eb96e981`](https://github.com/ansible/jewel/commit/c0e9eb96e9811afb28dccd72ee28f74e0c9d0266) 2026-09-30 [AAP-65516] Removing POST option from service_keys endpoint (#235)
- [`e09ebeded951`](https://github.com/ansible/jewel/commit/e09ebeded951db1e25211d682ecde488855d98b7) 2026-10-01 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 9fe7ebd (#261)
- [`9d11a9fe110c`](https://github.com/ansible/jewel/commit/9d11a9fe110c73f06c6a8a4ae26f88020eb18c54) 2026-10-01 test: exclude bulk-update endpoint from test_request_objects (#262)
- [`0f1b90f9f39a`](https://github.com/ansible/jewel/commit/0f1b90f9f39ac1bdd314b5f49c5e6b50312f3799) 2026-10-01 [AAP-95395] Upgrade PyJWT to safe version (#263)
- [`fbcb9fbe8c19`](https://github.com/ansible/jewel/commit/fbcb9fbe8c195331859da8b9c235c48a4ba310d4) 2026-10-02 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to bd27a48 (#265)
- [`b9ce7e85eb78`](https://github.com/ansible/jewel/commit/b9ce7e85eb78d9069fe54c4e8d1090ac308b4d86) 2026-10-02 fix(envoy): redirect bare API and service paths to trailing slashes (#234)
- [`6a4a37fe85f8`](https://github.com/ansible/jewel/commit/6a4a37fe85f81e1e6471487e0739d9a65d5809fe) 2026-10-02 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to a4ab29e (#266)
- [`a5e20b5361f6`](https://github.com/ansible/jewel/commit/a5e20b5361f61836e80c8eb4191615fff0d3e527) 2026-10-02 [AAP-38240] Migrate development environment to Podman (#245)
- [`33f0fa03aa48`](https://github.com/ansible/jewel/commit/33f0fa03aa485551ab838d5f70382ddf063a5335) 2026-10-06 [AAP-93722] add cleantext validation for settings preferences (#251)
- [`8ab082a453a8`](https://github.com/ansible/jewel/commit/8ab082a453a85c347ffddc110af1ee354d4ff2ed) 2026-10-06 [AAP-95488] Request Envoy specialist reviews (#271)
- [`6fc577a76c03`](https://github.com/ansible/jewel/commit/6fc577a76c03e0b4095a88f4dc05126f56b889d0) 2026-10-07 Add migration command code owner (#270)
- [`182dd1ee8f7c`](https://github.com/ansible/jewel/commit/182dd1ee8f7ccee386e68d13320e5768144a5844) 2026-10-08 fix: anchor awk pattern for DAB devel branch lookup (#276)
- [`f3de3fc4efec`](https://github.com/ansible/jewel/commit/f3de3fc4efec02d98c111ab7c456b42030d30676) 2026-10-08 Support manually built feature CI images (#275)
- [`a0b52048207a`](https://github.com/ansible/jewel/commit/a0b52048207a443642cc03d65fd8f99347245b0f) 2026-10-08 feat(envoy): Enable X25519MLKEM768 key exchange (#268)
- [`f79fbb196df4`](https://github.com/ansible/jewel/commit/f79fbb196df466f8c925031dd19c2b99c29892b2) 2026-10-08 [AAP-82819] fix: deduplicate CSRF trusted origins (#273)
- [`1e95ac30416e`](https://github.com/ansible/jewel/commit/1e95ac30416e130e37fc24b3da91902bc1bfd2b5) 2026-10-08 Fix CI image Podman preflight (#277)
- [`21a64d4febac`](https://github.com/ansible/jewel/commit/21a64d4febac435fc949f106ac6a128ce73754df) 2026-10-09 [AAP-96061] Add migration upgrade validation CI (#278)

### `ansible-ui` (`devel`)

`4c3403d95196` → `6fc15743d2ee` — 44 commits. [compare](https://github.com/ansible/ansible-ui/compare/4c3403d951965d7d0527926f564a122588ef9ece...6fc15743d2ee4b1e31c238c6bc78cef9309fa65c)

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

## Public image digests

Resolved from the development tag. Stable version tags are ignored.

| Component | Previous | Proposed | Note |
|-----------|----------|----------|------|
| `awx` | `ghcr.io/ansible/awx:devel@sha256:ae94fd1b7a17d22cd51e60919b4cfe78c549b9e1355aefac776a7d06c651ed3c` | `ghcr.io/ansible/awx:devel@sha256:79090c0fd5b551410871c951f2b9d239c832bdd63927357d7000920f562750c3` | development tag; stable versions are not used |
| `jewel` | `ghcr.io/ansible/jewel:latest@sha256:ed49c4cbd073eea03914913088fc97d75dcb4628651ca8d1a29b2c8258675ca0` | `ghcr.io/ansible/jewel:latest@sha256:399bb7f44f3021a876b86dbe6f6b9b923df41bb632f7267513977d91fdd26614` | development tag; stable versions are not used |

## Image tracks to consider

Cut a component tag only after review. Independent trains
(prefer one component per release unless you mean to rebake):

| Track | Suggested tag | Why |
|-------|---------------|-----|
| `platform-ui` | `platform-ui-v0.1.3` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-v0.1.3` | upstream moved: `jewel` |
| `awx` | — | upstream moved, but `components.awx.build` is false — record the digest, do not cut an awx image |

## Agent next step

1. Read the commits above. Hold a pin whose range is empty or unsafe to ship.
2. Keep `ref` on the development branch. `commit` is that branch's tip.
   `public_image_digest` is the matching image digest — do not substitute a
   stable version tag.
3. Bump `published.<component>.version` only for tracks whose triggers moved.
4. Render that component's notes (they include this commit list) and add a
   short narrative at the bottom:

```bash
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version X.Y.Z \
  --out release/notes/platform-ui-vX.Y.Z.md
```

5. Ask before tagging (`platform-ui-v*`, `jewel-with-ui-v*`) or publishing.

## Operator handoff

After a component is actually released:

1. Bump **only** that image in `awx-platform-operator` → `release/pins.consumer.yaml`.
2. Leave other component pins unchanged.
3. See `release/AGENTS.md`.

