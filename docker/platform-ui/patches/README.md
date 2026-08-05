# ansible-ui build patches

Patches here are applied **at image build time** against a clean copy of the
`ansible-ui` tree (see `docker/platform-ui/Dockerfile`). The `ansible-ui/` git
checkout stays unmodified so you can `git pull` / retarget tags without
carrying local commits.

Broader build docs and research: [README.md](../../../README.md),
[docs/DISCOVERIES.md](../../../docs/DISCOVERIES.md).

## Apply order

Files are applied in shell glob order:

```text
0001-....patch
0002-....patch
...
```

Use a numeric prefix. Paths inside each patch must be relative to the monorepo
root (e.g. `platform/main/PlatformApp.tsx`) with `patch -p1` strip level
(git-style `a/` / `b/` prefixes).

## Creating a new patch

```bash
cd ansible-ui
# edit files...
git diff > ../docker/platform-ui/patches/0002-my-change.patch
git checkout -- .
```

Then rebuild:

```bash
make build-ui
# or full jewel image with UI baked in:
make build-jewel
```

## Current patches

| Patch | Purpose |
|-------|---------|
| `0001-skip-subscription-banner-for-open-license.patch` | Hide AAP “subscription out of compliance” banners when Controller reports `license_type: open` (upstream AWX). |
