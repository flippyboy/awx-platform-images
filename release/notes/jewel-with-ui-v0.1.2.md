# jewel-with-ui 0.1.2

Independent component release. Git tag: `jewel-with-ui-v0.1.2`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:0.1.2`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:0.1.2`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

`ghcr.io/ansible/jewel:latest@sha256:ed49c4cbd073eea03914913088fc97d75dcb4628651ca8d1a29b2c8258675ca0`

Development image (`latest` / `devel`). A pinned digest is what the release build pulls. Stable upstream version tags are not used.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `b68b6cabaa22 via devel` | `e680bd860a58 via devel` | [compare](https://github.com/ansible/jewel/compare/b68b6cabaa2214221c7eff816b1cd9e04061b7db...e680bd860a58db23380c0b12807d31cab71856ef) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`b68b6cabaa22` → `e680bd860a58` — 32 commits. [compare](https://github.com/ansible/jewel/compare/b68b6cabaa2214221c7eff816b1cd9e04061b7db...e680bd860a58db23380c0b12807d31cab71856ef)

- [`04baec0c2d24`](https://github.com/ansible/jewel/commit/04baec0c2d24ce9ff244c0b6dfedbb6be03cedba) 2026-08-26 Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to fd3ca0a (#212)
- [`65626c567ccd`](https://github.com/ansible/jewel/commit/65626c567ccd120e9e6f120a60b89c6947716711) 2026-08-27 [AAP-76998] Fix Envoy outlier detection ejecting controller on WebSocket teardowns (#114)
- [`e7c3d8485026`](https://github.com/ansible/jewel/commit/e7c3d8485026f09f225cf3ce66b02403dd01d7b8) 2026-08-27 [AAP-76853] Fix initialize_preferences() abort on single preference failure (#150)
- [`a2a80401b749`](https://github.com/ansible/jewel/commit/a2a80401b749abfe6c67ff67489f49ee1c30fda8) 2026-08-31 [AAP-88564] Optimize CI with pre-built container image (#208)
- [`b574fda1b959`](https://github.com/ansible/jewel/commit/b574fda1b959bef849b3844c86801cd7f6b39ead) 2026-08-31 Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 87e16a0 (#221)
- [`4991ed2475d7`](https://github.com/ansible/jewel/commit/4991ed2475d747495effc7c4a95160b40c7ed84e) 2026-09-01 [AAP-90662] Pin sqlparse>=0.6.0 for CVE-2026-59893 (#223)
- [`ea52052e1238`](https://github.com/ansible/jewel/commit/ea52052e1238b44ea35aee0098dc33ce3481b542) 2026-09-01 [AAP-90726] Note sqlparse>=0.6.0 also fixes CVE-2026-71491 (#224)
- [`389e86fcc31a`](https://github.com/ansible/jewel/commit/389e86fcc31aabe4fcc998f9651338e38bc2fd16) 2026-09-01 [AAP-89439] Restore DABCacheWithFallback as default cache backend (#220)
- [`33df5a0a8f9d`](https://github.com/ansible/jewel/commit/33df5a0a8f9d68101b244be6b06b45d1a87c5868) 2026-09-01 Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 2484027 (#222)
- [`87499baa31d8`](https://github.com/ansible/jewel/commit/87499baa31d8585eebe4bfc19b7d22657545d656) 2026-09-02 AAP-85286: Do not treat rewritten service_id as empty registry (#215)
- [`102fe5cea307`](https://github.com/ansible/jewel/commit/102fe5cea307b4eeb3c2c9ddcecfe0117d14b7a6) 2026-09-02 Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to b85009e (#226)
- [`7ef38f996341`](https://github.com/ansible/jewel/commit/7ef38f996341dfbef6376ebc3e1eb5bde97db994) 2026-09-02 Prefix Renovate Tekton commits with NO_JIRA: (#227)
- [`558e2ca29e8d`](https://github.com/ansible/jewel/commit/558e2ca29e8d15b19e10ee40f36fd2e97b2fd030) 2026-09-08 AAP-91661 | fix: remove tests for deleted FEATURE_INDIRECT_NODE_COUNTING_ENABLED (#228)
- [`a7f928de8b65`](https://github.com/ansible/jewel/commit/a7f928de8b65f4aee4d0a906276fe9fcaef07556) 2026-09-08 AAP-91661 | fix: feature flag test still uses database (#232)
- [`64dd6213c7ab`](https://github.com/ansible/jewel/commit/64dd6213c7ab2ff5969f4d93e2d4e8b0fb9f3e78) 2026-09-09 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to a548629 (#231)
- [`50b7db90cd8b`](https://github.com/ansible/jewel/commit/50b7db90cd8b27def3e8c819db92f41326ae0f19) 2026-09-10 [AAP-78708] Add CleanTextMixin to Gateway serializers (#219)
- [`f03f0d09350a`](https://github.com/ansible/jewel/commit/f03f0d09350a198d1c15772cc0a84f55124df232) 2026-09-10 [AAP-92202] Fix: do not cache empty xDS CDS/LDS responses during bootstrap (#233)
- [`a72137dc304b`](https://github.com/ansible/jewel/commit/a72137dc304bc246738c0aae7c8e3f4618486f8a) 2026-09-15 [AAP-92807] Gate merge-ready label on Konflux (#238)
- [`901fe4cc9e5b`](https://github.com/ansible/jewel/commit/901fe4cc9e5be1182b4e42040842f1f52251f8bd) 2026-09-16 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 40e7aac (#236)
- [`84c081ccc375`](https://github.com/ansible/jewel/commit/84c081ccc37546c442edb3d04d1aa898687ad2fe) 2026-09-17 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 27d0417 (#240)
- [`5e6579f61b18`](https://github.com/ansible/jewel/commit/5e6579f61b18f485f7ab87abad82ce48cf88b1f3) 2026-09-17 [AAP-64014] Stop logging expected API root lookup misses as ERROR (#225)
- [`6e88eb179bdd`](https://github.com/ansible/jewel/commit/6e88eb179bddb8577cfeb15e23bcd3539cb0a8ea) 2026-09-18 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 27cd6cb (#242)
- [`f63756550e27`](https://github.com/ansible/jewel/commit/f63756550e2795bf1b5c914fe04275ecffa365c0) 2026-09-18 [AAP-82386] Fix remaining SonarCloud findings (#241)
- [`ab23ce6ab18d`](https://github.com/ansible/jewel/commit/ab23ce6ab18d43677162a9f48bb2409970ff37b9) 2026-09-21 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 975248e (#244)
- [`bbf25f06d053`](https://github.com/ansible/jewel/commit/bbf25f06d0530cb0f9bc508b7e89ccca7025db56) 2026-09-23 [AAP-76717]: Resolve remaining SonarCloud findings (#248)
- [`4e3eaffe328e`](https://github.com/ansible/jewel/commit/4e3eaffe328e01b8368bf5a3cf25cfc9aae743d2) 2026-09-24 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 27ae7a0 (#253)
- [`0014f0409779`](https://github.com/ansible/jewel/commit/0014f0409779010881091c7f5bbd238d559786da) 2026-09-24 [AAP-59800] Reduce complexity in create_preload_data (#247)
- [`7af9132127c6`](https://github.com/ansible/jewel/commit/7af9132127c657f3ec43e7beea59a9c19e7c025a) 2026-09-24 [AAP-91996] Sync to service first to populate parent_reference on ObjectRole (#249)
- [`58969661f396`](https://github.com/ansible/jewel/commit/58969661f3966ad717448ab161689396e2072a9a) 2026-09-24 [AAP-94199] Clear stale xDS cache on Gateway startup (#255)
- [`22be616e60d9`](https://github.com/ansible/jewel/commit/22be616e60d9f8e142673f3611db63625ab4f940) 2026-09-25 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to e4b9731 (#256)
- [`7aaac6d39400`](https://github.com/ansible/jewel/commit/7aaac6d394008af4d781e2107ed576c79da48c8c) 2026-09-25 AAP-94447 Fix migration history across 2.6 through devel (#258)
- [`e680bd860a58`](https://github.com/ansible/jewel/commit/e680bd860a58db23380c0b12807d31cab71856ef) 2026-09-25 AAP-72425: Cover username self-edit policy (#250)

## Operator handoff

1. Bump **only** `jewel-with-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.2` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
4. Cut an operator release only when the operator itself or chart defaults need a ship.

## Notes

jewel `devel` moved 32 commits past the 0.1.1 pin (`b68b6cabaa22` →
`e680bd860a58`). The image build pulls
`ghcr.io/ansible/jewel:latest@sha256:ed49c4cbd073…` and bakes platform-ui
0.1.2, which is published in the same pins update.

Notable changes in that range: sqlparse pinned for CVE-2026-59893 and
CVE-2026-71491, Envoy outlier detection no longer ejects the controller on
WebSocket teardown, and the gateway no longer caches empty or stale xDS
responses across startup. The commit list above is the full changelog.

`components.awx.build` stays false. The awx devel tip and
`ghcr.io/ansible/awx:devel` digest are recorded in `pins.yaml` and no awx
image is cut.

