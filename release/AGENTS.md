# Agent instructions: pins, cadence, release notes

You are assisting with **steady-cadence component releases** for `awx-platform-images`.

## Hard rules

1. **Never fork or vendor** `ansible/awx`, `ansible/jewel`, or `ansible/ansible-ui` into this repo.
2. Only change **`pins.yaml`** (and generated notes). Dockerfiles may gain patches, not full app trees.
3. Prefer **commit SHAs** for any pin that will ship in a tagged release.
4. Record **why** a pin moved (security, bugfix, feature) in release notes.
5. Do not push tags or publish packages unless the user explicitly asks.

## Workflow

### A. Propose pins (weekly / on demand)

```bash
python release/propose-pins.py \
  --pins pins.yaml \
  --out pins.proposed.yaml \
  --github-token "$GITHUB_TOKEN"   # optional; higher API rate limit
```

Review `pins.proposed.yaml`:

- For each component, decide: keep previous commit, move to newest semver tag, or track branch tip.
- Use `release/cadence.yaml` → `agent_preferences`.
- Write decisions into `pins.yaml` (merge by hand or `mv pins.proposed.yaml pins.yaml` after review).

### B. Generate release notes

```bash
# Save previous pins before merge
cp pins.yaml pins.prev.yaml   # once, before editing

python release/render-notes.py \
  --prev pins.prev.yaml \
  --curr pins.yaml \
  --version images-v0.1.0 \
  --out release/notes/images-v0.1.0.md
```

Notes must include:

- Table of component → old SHA → new SHA / tag
- Upstream compare links (`https://github.com/ansible/<repo>/compare/<old>...<new>`)
- Operator handoff checklist (digest bump PR for `awx-platform-operator`)

### C. Build & release (CI)

Tag `images-vX.Y.Z` after pins merge. CI builds/pushes images and attaches notes.

### D. Operator handoff

Open or draft PR on **awx-platform-operator**:

- Update `release/pins.consumer.yaml` digests
- Update Helm chart default image tags if needed
- Reference `images-vX.Y.Z` in operator release notes

## Decision rubric (tags)

| Situation | Prefer |
|-----------|--------|
| Upstream has new patch tag, our pin is older tag | Move to newest matching semver tag, resolve to SHA |
| Only floating branch (`devel`) | Capture current branch tip SHA; note “tracking devel” |
| No meaningful commits since last release | **Do not** cut images release; skip cadence |
| Breaking / large churn | Call out in notes; consider holding pin |

## Output style for chat agents

When reporting to the user:

1. Summary table (component / previous / proposed / reason)
2. Recommended release version (`images-v…`)
3. Draft release notes path
4. Explicit ask before tagging or publishing
