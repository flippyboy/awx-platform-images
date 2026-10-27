# Agent instructions: pins, cadence, **per-component** releases

You are assisting with **independent component releases** for `awx-platform-images`.

Each publishable image has its **own** version and git tag. Do **not** cut a monolithic
`images-v*` release that ships every image together.

| Component | Git tag | GHCR image |
|-----------|---------|------------|
| `platform-ui` | `platform-ui-vYYYY.MM.DD` | `ghcr.io/flippyboy/awx/platform-ui:YYYY.MM.DD` |
| `jewel-with-ui` | `jewel-with-ui-vYYYY.MM.DD` | `ghcr.io/flippyboy/awx/jewel-with-ui:YYYY.MM.DD` |
| `awx` (optional) | `awx-vYYYY.MM.DD` | `ghcr.io/flippyboy/awx/awx:YYYY.MM.DD` |

Image versions are **calver**, not semver. `YYYY.MM.DD` is the UTC date of the cut,
with zero-padded month and day (`2026.10.21`). A later cut the same day appends
`-N`, and N starts at 1 (`2026.10.21-1`). The published `0.1.x` tags are the last
semver cuts. Do not bump those numbers.

`jewel-with-ui` **bakes** a already-published `platform-ui` tag (see
`published.jewel-with-ui.platform_ui_version`). Releasing UI does not automatically
rebake jewel; release jewel separately when you want the new UI inside it.

## Hard rules

1. **Never fork or vendor** `ansible/awx`, `ansible/jewel`, or `ansible/ansible-ui` into this repo.
2. Only change **`pins.yaml`** (and generated notes). Dockerfiles may gain patches, not full app trees.
3. Pin the **development-branch tip** (`devel`, or `main` when that is the default) as a commit SHA. For public images, also pin `public_image_digest` from the floating development tag (`ghcr.io/ansible/awx:devel`, `ghcr.io/ansible/jewel:latest`). Stable semver tags and stable image versions lag that line by years and must not be used.
4. Record **why** a pin moved (security, bugfix, feature) in release notes. The changelog is the upstream commits on the development branch since the previous pin.
5. Do not push tags or publish packages unless the user explicitly asks.
6. **Release only components whose inputs changed** (or that the user asked for).
7. **New image tags are calver** `YYYY.MM.DD`, or `YYYY.MM.DD-N` for another cut that
   UTC day. Do not mint `0.x.y` image tags.

## Workflow

### A. Propose pins (weekly / on demand)

```bash
python release/propose-pins.py \
  --pins pins.yaml \
  --out pins.proposed.yaml \
  --github-token "$GITHUB_TOKEN"   # optional; higher API rate limit

python release/render-notes.py \
  --prev pins.yaml \
  --curr pins.proposed.yaml \
  --proposal \
  --out release/notes/PROPOSED.md
```

Review `pins.proposed.yaml` and `release/notes/PROPOSED.md`:

- `ref` stays on the development branch (`devel` or `main`). `commit` is that branch's tip SHA.
- `public_image_digest` is the registry digest of the floating development image (`awx:devel`, `jewel:latest`).
- `PROPOSED.md` lists the upstream commits since the current pin. That list is the changelog for the component release.
- Reject a proposal that moves a pin onto a stable tag (`24.6.x`, `v2.4.x`, `stable`).
- Use `release/cadence.yaml` → `agent_preferences`.
- Write accepted decisions into `pins.yaml`. Merging the proposal is not itself a release.

### B. Decide which image(s) to cut

Map pin changes → image tracks (`release/cadence.yaml` / `derived.*.release_triggers`):

| Upstream pin moved | Consider releasing |
|--------------------|--------------------|
| `ansible-ui` | `platform-ui` (then optionally `jewel-with-ui` to rebake) |
| `jewel` / jewel base image | `jewel-with-ui` |
| `awx` and `build: true` | `awx` |

Set only that track’s `published.<component>.version` in `pins.yaml` to the UTC
calver. The first cut that day is `YYYY.MM.DD`. If that date is already published,
use `YYYY.MM.DD-1`, then `-2`, and so on.

### C. Generate release notes (per component)

The rendered notes include the upstream commit list. Add a short narrative under `## Notes` (why this cut, known issues). Do not replace the commit list with a stable-tag summary.

```bash
cp pins.yaml pins.prev.yaml   # once, before editing pins

python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.10.21 \
  --out release/notes/platform-ui-v2026.10.21.md

# jewel-with-ui example (pin which UI image is baked)
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component jewel-with-ui \
  --version 2026.10.21 \
  --platform-ui-version 2026.10.21 \
  --out release/notes/jewel-with-ui-v2026.10.21.md

# second cut the same UTC day
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 2026.10.21-1 \
  --out release/notes/platform-ui-v2026.10.21-1.md
```

### D. Build & release (CI)

After pins + notes merge to `main`:

```bash
# UI only
git tag platform-ui-v2026.10.21 && git push origin platform-ui-v2026.10.21

# Jewel only (pulls published platform-ui from GHCR)
git tag jewel-with-ui-v2026.10.21 && git push origin jewel-with-ui-v2026.10.21

# Later the same day
git tag platform-ui-v2026.10.21-1 && git push origin platform-ui-v2026.10.21-1
```

Or use **Actions → release-images → Run workflow** with component + version.

CI pushes only that image and opens a GitHub Release named e.g. `platform-ui 2026.10.21`.
The `jewel-with-ui` build pulls `components.jewel.public_image` at `public_image_digest` (the development image, not a stable version).

After the image is pushed, `release-images` dispatches `images-released` on
**awx-platform-operator** with this component, tag, and digest. That repo pins
the image and pushes the next operator calver tag. Do not open a separate pin
PR for the same image.

### E. Operator handoff

The release workflow does this. It is not a manual pull request.

- `platform-ui` updates only that pin. The gateway image stays until `jewel-with-ui` is released.
- `jewel-with-ui` updates the gateway chart and role defaults.
- `awx` updates the controller pin only when `components.awx.build` is true and this repo published `awx-v*`.
- The controller otherwise stays `ghcr.io/ansible/awx` pinned by digest. See [`docs/awx-image.md`](../docs/awx-image.md).

## Decision rubric

| Situation | Prefer |
|-----------|--------|
| Development branch has new commits | Pin the tip SHA. Use the commit subjects as the release changelog. Cut the image whose trigger moved. |
| Upstream stable/semver tag exists | Leave it. Those tags lag `devel` / `main` by years. |
| Public development image moved (`awx:devel`, `jewel:latest`) | Record `public_image_digest`. Do not switch to a stable image version. |
| No meaningful commits since last **this** component’s release | **Do not** cut that component; skip |
| Only UI changed | Cut `platform-ui`; cut `jewel-with-ui` only if you want UI rebaked into gateway |
| Breaking / large churn | Call out in notes; consider holding pin |

## Output style for chat agents

When reporting to the user:

1. Summary table (upstream / previous / proposed / reason)
2. **Which image track(s)** to release (not a single umbrella version)
3. Recommended tags (`platform-ui-v…`, `jewel-with-ui-v…`)
4. Draft release notes path(s)
5. Explicit ask before tagging or publishing
