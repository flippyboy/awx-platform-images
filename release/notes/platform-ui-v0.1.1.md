# platform-ui 0.1.1

Independent component release. Git tag: `platform-ui-v0.1.1`.

## Image

`ghcr.io/flippyboy/awx/platform-ui:0.1.1`

## Upstream pins (relevant)

| Upstream | Previous | New | Link |
|----------|----------|-----|------|
| ansible-ui | `devel` (unpinned) | `6fe43c634d1a` via `devel` | https://github.com/ansible/ansible-ui |

**1** relevant upstream pin(s) changed.

## Notes

First commit-SHA pin for `ansible-ui`. 0.1.0 built from floating `devel`; this cut records
`6fe43c634d1affa5e82ef0529f4412869c8d8fca` (2026-08-25, AAP-85025 report-management
copy) so the image is reproducible.

Rejected latest GitHub semver tag `v2.4.313` (2023-08-15): ansible-ui no longer
publishes tags, and that line is years behind `devel`. Cadence still prefers
semver when tags are current.

## Operator handoff

1. Bump **only** `platform-ui` in `awx-platform-operator` → `release/pins.consumer.yaml`
   (tag `0.1.1` + digest once available).
2. Update Helm chart default image tag for this component if it is a chart default.
3. Leave other component pins unchanged — they have independent release trains.
