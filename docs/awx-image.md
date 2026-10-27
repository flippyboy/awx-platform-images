# AWX controller image

Pin the upstream development image by digest in the operator release. Do not build a second controller image in this repo, and do not give that image a semver.

## What ships today

`components.awx.build` is false. Compose still pulls `ghcr.io/ansible/awx:devel`. This repo records that tag's digest in `components.awx.public_image_digest`. `docker/awx/Dockerfile` is `FROM` that image and adds nothing. The operator pulls the same image by digest once `propose-awx-pin` has been merged and an operator release is cut. Until that release, the operator chart still has `image_version: devel`.

Upstream semver tags (`24.6.x`) lag `devel` by years. A semver we minted (`0.1.x`) would not be upstream's version, and it would bring back the scheme the other images just left.

## Pin the digest

The operator is what a cluster pulls. A floating `:devel` tag moves without an operator release, so the next install can run a different controller than the one that was tested.

Keep the image name `ghcr.io/ansible/awx`. The operator repo chooses the pull. `.github/workflows/propose-awx-pin.yml` there resolves `devel` on `ansible/awx` and the digest of `ghcr.io/ansible/awx:devel`, then opens a review pull request. That pull request:

- records `git_commit` and `digest` on `images.awx` in `release/pins.consumer.yaml`
- sets controller `image_version` to the digest
- lists the upstream commits since the previous pin in `release/notes/PROPOSED-awx.md`

The installer pulls `ghcr.io/ansible/awx@sha256:…` when `image_version` is a digest. `devel` stays the tracking label in the pin file. Do not move this pin onto an upstream stable tag.

Merging the proposal does not tag an operator release. The next operator release copies the commit list into its release notes. A `platform-ui` or `jewel-with-ui` publish does not move this pin. This repo's `components.awx.public_image_digest` is the digest recorded for image builds here. It is not the cluster pull.

## When a build here is the right tool

Build `ghcr.io/flippyboy/awx/awx` only when the controller image needs a patch this repo owns, the way `platform-ui` patches ansible-ui. Then:

1. Set `components.awx.build: true`.
2. Cut `awx-vYYYY.MM.DD` with the same calendar version as the other images. Not semver.
3. The image release dispatches `images-released`. The operator pins `ghcr.io/flippyboy/awx/awx:<calver>` plus that digest and drops `ghcr.io/ansible/awx`.

A calendar tag on an unmodified `FROM ghcr.io/ansible/awx:devel` image is a second name for a digest we already have. Don't add it.
