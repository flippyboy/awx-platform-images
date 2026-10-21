# jewel-with-ui 0.1.3

Independent component release. Git tag: `jewel-with-ui-v0.1.3`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:0.1.3`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:0.1.3`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Jewel base image

`ghcr.io/ansible/jewel:latest@sha256:748fcc338ea3d651601903070bc104bd11a890514cf091da6e46a6be54171ed7`

Development image (`latest` / `devel`). A pinned digest is what the release build pulls. Stable upstream version tags are not used.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `e680bd860a58 via devel` | `b9eb41abe310 via devel` | [compare](https://github.com/ansible/jewel/compare/e680bd860a58db23380c0b12807d31cab71856ef...b9eb41abe31025e6a3c27fe25c36007a12de877d) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `jewel` (`devel`)

`e680bd860a58` → `b9eb41abe310` — 29 commits. [compare](https://github.com/ansible/jewel/compare/e680bd860a58db23380c0b12807d31cab71856ef...b9eb41abe31025e6a3c27fe25c36007a12de877d)

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
- [`bc31427e376d`](https://github.com/ansible/jewel/commit/bc31427e376ddba5bcb1c296c729d7180c0b5211) 2026-10-12 [AAP-96929] Fall back via startswith prefix in get_pr_checkout (#287)
- [`f3f749494544`](https://github.com/ansible/jewel/commit/f3f749494544a4c4bd1e108f91ecb4244f5ff84a) 2026-10-13 [AAP-96856] Pull CI service images from trusted registries instead of Docker Hub (#285)
- [`e6f932e7277d`](https://github.com/ansible/jewel/commit/e6f932e7277dc68a067d0f7c9bead37c7413e2a7) 2026-10-13 build(deps): upgrade urllib3 to >=2.8.0 (#289)
- [`bda0d472fddb`](https://github.com/ansible/jewel/commit/bda0d472fddb115d8108df344cc493b90b1a67f5) 2026-10-14 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 8214af8 (#286)
- [`5c9b28cadd6e`](https://github.com/ansible/jewel/commit/5c9b28cadd6e09ae6ee1c193c9d77d19084c1616) 2026-10-14 [AAP-96855] Pull devel observability sidecars from trusted registries instead of Docker Hub (#284)
- [`45b04e979b69`](https://github.com/ansible/jewel/commit/45b04e979b69f39a2c2887bd181a017c3fbbc506) 2026-10-14 Configure CI image branch selection per repository (#291)
- [`63129fb4cf5c`](https://github.com/ansible/jewel/commit/63129fb4cf5c501054ca4ca73ad6b7691bf80e66) 2026-10-14 [AAP-96929] Fall back via endswith suffix in get_pr_checkout (#290)
- [`5e34446ce4ac`](https://github.com/ansible/jewel/commit/5e34446ce4acbd6d32a4c549d223ba5f0b340f0e) 2026-10-15 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 4ffd901 (#293)
- [`cc3bcdf13403`](https://github.com/ansible/jewel/commit/cc3bcdf134037ecd8c0a0429640b942b74551b2b) 2026-10-16 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to 673c5ba (#294)
- [`31f57ac5f212`](https://github.com/ansible/jewel/commit/31f57ac5f212adeca13aeef2d8aa999cb7bafac7) 2026-10-19 NO_JIRA: Update quay.io/aap-ci/tekton-catalog/pipeline/test/aap-api-tests:0.1 Docker digest to c94a8ad (#298)
- [`acecb43bc379`](https://github.com/ansible/jewel/commit/acecb43bc37977631faca49259b4073a980dc3f3) 2026-10-19 fix: migration references (#297)
- [`b9eb41abe310`](https://github.com/ansible/jewel/commit/b9eb41abe31025e6a3c27fe25c36007a12de877d) 2026-10-19 AAP-94168 immediate sync of assigned permissions (#264)

## Operator handoff

1. Bump **only** `jewel-with-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.3` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
4. Cut an operator release only when the operator itself or chart defaults need a ship.

## Notes

jewel `devel` moved 29 commits past the 0.1.2 pin (`e680bd860a58` → `b9eb41abe310`). This release also bakes the newly published `platform-ui:0.1.3`. Notable: Envoy path redirects and key exchange, PyJWT and urllib3 security upgrades, migration tooling, and immediate permission sync. The commit list above is the full changelog.

