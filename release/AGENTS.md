# Agent instructions: pins, cadence, **per-component** releases

You are assisting with **independent component releases** for `awx-platform-images`.

Each publishable image has its **own** version and git tag. Do **not** cut a monolithic
`images-v*` release that ships every image together.

| Component | Git tag | GHCR image |
|-----------|---------|------------|
| `platform-ui` | `platform-ui-vX.Y.Z` | `ghcr.io/flippyboy/awx/platform-ui:X.Y.Z` |
| `jewel-with-ui` | `jewel-with-ui-vX.Y.Z` | `ghcr.io/flippyboy/awx/jewel-with-ui:X.Y.Z` |
| `awx` (optional) | `awx-vX.Y.Z` | `ghcr.io/flippyboy/awx/awx:X.Y.Z` |

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

Bump only that track’s `published.<component>.version` in `pins.yaml`.

### C. Generate release notes (per component)

The rendered notes include the upstream commit list. Add a short narrative under `## Notes` (why this cut, known issues). Do not replace the commit list with a stable-tag summary.

```bash
cp pins.yaml pins.prev.yaml   # once, before editing pins

python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component platform-ui \
  --version 0.1.1 \
  --out release/notes/platform-ui-v0.1.1.md

# jewel-with-ui example (pin which UI image is baked)
python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --component jewel-with-ui \
  --version 0.1.1 \
  --platform-ui-version 0.1.1 \
  --out release/notes/jewel-with-ui-v0.1.1.md
```

### D. Build & release (CI)

After pins + notes merge to `main`:

```bash
# UI only
git tag platform-ui-v0.1.1 && git push origin platform-ui-v0.1.1

# Jewel only (pulls published platform-ui from GHCR)
git tag jewel-with-ui-v0.1.1 && git push origin jewel-with-ui-v0.1.1
```

Or use **Actions → release-images → Run workflow** with component + version.

CI pushes only that image and opens a GitHub Release named e.g. `platform-ui 0.1.1`.
The `jewel-with-ui` build pulls `components.jewel.public_image` at `public_image_digest` (the development image, not a stable version).

### E. Operator handoff

Open or draft PR on **awx-platform-operator**:

- Update **only** the released image(s) in `release/pins.consumer.yaml`
- Update Helm chart defaults for those images if needed
- Reference the component tag(s) (`platform-ui-v…`, `jewel-with-ui-v…`) in operator notes
- Other component pins stay put

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
