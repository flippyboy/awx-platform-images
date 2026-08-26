# jewel-with-ui 0.1.1

Independent component release. Git tag: `jewel-with-ui-v0.1.1`.

## Image

`ghcr.io/flippyboy/awx/jewel-with-ui:0.1.1`

## Baked platform-ui

`ghcr.io/flippyboy/awx/platform-ui:0.1.1`

This release does **not** rebuild platform-ui; it pulls the published UI image above.

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| jewel | `devel` (unpinned) | `b68b6cabaa22` via `devel` | https://github.com/ansible/jewel |

**1** relevant upstream pin(s) changed.

Jewel still has no semver tags; image build continues to use
`ghcr.io/ansible/jewel:latest`. The git SHA is for tracking.

## Notes

- Pin jewel `devel` at `b68b6cabaa2214221c7eff816b1cd9e04061b7db` (2026-08-25, SECURITY.md).
- Intentionally rebake **platform-ui 0.1.1** (ansible-ui `6fe43c634d1a`) into the gateway.

## Operator handoff

1. Bump **only** `jewel-with-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.1` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
