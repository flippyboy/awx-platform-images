# AWX controller image

Pin the upstream development image by digest in the operator release. Do not build a second controller image in this repo, and do not give that image a semver.

## What ships today

`components.awx.build` is false. Compose and the operator pull `ghcr.io/ansible/awx:devel`. This repo records that tag's digest in `components.awx.public_image_digest`. `docker/awx/Dockerfile` is `FROM` that image and adds nothing.

Upstream semver tags (`24.6.x`) lag `devel` by years. A semver we minted (`0.1.x`) would not be upstream's version, and it would bring back the scheme the other images just left.

## Pin the digest

The operator is what a cluster pulls. A floating `:devel` tag moves without an operator release, so the next install can run a different controller than the one that was tested.

Keep the image name `ghcr.io/ansible/awx`. On each operator release, set the pull to the digest this repo already recorded:

```text
ghcr.io/ansible/awx@sha256:…
```

`image_version` can stay `devel` as the human-readable label. The digest is what makes the pull reproducible. Do not move this pin onto an upstream stable tag.

That digest update is not an image build. It does not need an `awx-v*` tag. The operator release that follows a `platform-ui` or `jewel-with-ui` publish should copy the current `public_image_digest` into `release/pins.consumer.yaml` when that handoff grows a digest field. Until then, the operator keeps the controller pin it last shipped (`devel`, no digest).

## When a build here is the right tool

Build `ghcr.io/flippyboy/awx/awx` only when the controller image needs a patch this repo owns, the way `platform-ui` patches ansible-ui. Then:

1. Set `components.awx.build: true`.
2. Cut `awx-vYYYY.MM.DD` with the same calendar version as the other images. Not semver.
3. The image release dispatches `images-released`. The operator pins `ghcr.io/flippyboy/awx/awx:<calver>` plus that digest and drops `ghcr.io/ansible/awx`.

A calendar tag on an unmodified `FROM ghcr.io/ansible/awx:devel` image is a second name for a digest we already have. Don't add it.
