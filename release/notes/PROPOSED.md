# Proposed pin update

Automated weekly proposal. **Review before merge.** This is not a release.

Generated from pin delta (`pins.prev.yaml` → `pins.proposed.yaml`).

## Upstream pins

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `6fe43c634d1a via devel` | `bfb91000abb9 via v2.4.313` | [compare](https://github.com/ansible/ansible-ui/compare/6fe43c634d1affa5e82ef0529f4412869c8d8fca...bfb91000abb9e3e106a1c01eb3c8efedae643ee5) |
| awx | `eb7090dd0f93 via devel` | `94e5795dfc37 via 24.6.1` | [compare](https://github.com/ansible/awx/compare/eb7090dd0f93d48d984c835639834979b5b17028...94e5795dfc37b95c576d61f3e3b4e936c021548c) |
| jewel | `b68b6cabaa22 via devel` | `ab23ce6ab18d via devel` | [compare](https://github.com/ansible/jewel/compare/b68b6cabaa2214221c7eff816b1cd9e04061b7db...ab23ce6ab18d43677162a9f48bb2409970ff37b9) |

**3** upstream pin(s) changed.

## Image tracks to consider

Cut a component tag only after review. Independent trains:

| Track | Git tag | Why |
|-------|---------|-----|
| `platform-ui` | `platform-ui-vX.Y.Z` | upstream moved: `ansible-ui` |
| `jewel-with-ui` | `jewel-with-ui-vX.Y.Z` | upstream moved: `jewel` |
| `awx` | `awx-vX.Y.Z` | skipped (`components.awx.build` is false) |

## Operator handoff

After a component is actually released:

1. Bump **only** that image in `awx-platform-operator` → `release/pins.consumer.yaml`.
2. Leave other component pins unchanged.
3. See `release/AGENTS.md`.

## Notes

_Agent/human: accept, hold, or revert individual pins before merge._

