# platform-ui 2026.11.02

Independent component release. Git tag: `platform-ui-v2026.11.02`.

Generated from pin delta (`pins.prev.yaml` → `pins.yaml`).

## Image

`ghcr.io/flippyboy/awx/platform-ui:2026.11.02`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `e7017aada0ba via devel` | `8b64849d386e via devel` | [compare](https://github.com/ansible/ansible-ui/compare/e7017aada0ba1334f70699aea58012dcfe4fe60a...8b64849d386e41bfbe1c3ce4d7d2722092cc1039) |

**1** relevant upstream pin(s) changed.

## Upstream commits

Changes on the development branch since the previous pin. This is the changelog for the release.

### `ansible-ui` (`devel`)

`e7017aada0ba` → `8b64849d386e` — 1 commits. [compare](https://github.com/ansible/ansible-ui/compare/e7017aada0ba1334f70699aea58012dcfe4fe60a...8b64849d386e41bfbe1c3ce4d7d2722092cc1039)

- [`8b64849d386e`](https://github.com/ansible/ansible-ui/commit/8b64849d386e41bfbe1c3ce4d7d2722092cc1039) 2026-10-30 AAP-95527 XLAB Address low priority Automation Dashboard review comments (#3841)

## Operator handoff

Publishing this image dispatches `images-released` on `awx-platform-operator`.
That workflow pins `platform-ui` `2026.11.02` (tag + digest) and cuts the
next operator calendar release. Other component pins stay put.

## Notes

Pins ansible-ui to the latest devel tip for minor Automation Dashboard review comment fixes (AAP-95527). No known issues. Upstream commits serve as the changelog.
