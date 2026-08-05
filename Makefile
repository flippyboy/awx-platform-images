# awx-platform-images
COMPOSE ?= $(shell docker compose version >/dev/null 2>&1 && echo "docker compose" || echo "docker-compose")
DOCKER  ?= docker

PLATFORM_UI_IMAGE ?= awx-compose/platform-ui:local
JEWEL_IMAGE       ?= awx-compose/jewel:local
JEWEL_BASE_IMAGE  ?= ghcr.io/ansible/jewel:latest
AWX_IMAGE         ?= ghcr.io/ansible/awx:devel
REGISTRY          ?= ghcr.io/flippyboy

.PHONY: help build build-ui build-jewel up down trust pins-propose notes fetch-upstream

help:
	@echo "Images / compose"
	@echo "  make build          platform-ui + jewel-with-ui"
	@echo "  make up / down      compose stack"
	@echo "  make trust          JWT bootstrap (compose)"
	@echo "Release / pins"
	@echo "  make pins-propose   write pins.proposed.yaml"
	@echo "  make fetch-upstream clone ansible/* at pins into .upstream/"

build-ui:
	./scripts/prepare-ui-context.sh
	$(DOCKER) build -f .build/ui-context/docker/platform-ui/Dockerfile \
		-t $(PLATFORM_UI_IMAGE) .build/ui-context

build-jewel: build-ui
	$(DOCKER) build -f docker/jewel/Dockerfile \
		--build-arg JEWEL_BASE=$(JEWEL_BASE_IMAGE) \
		--build-arg UI_IMAGE=$(PLATFORM_UI_IMAGE) \
		-t $(JEWEL_IMAGE) .

build: build-jewel

up: build
	$(COMPOSE) -f compose/docker-compose.yml --project-directory . up -d --remove-orphans

down:
	$(COMPOSE) -f compose/docker-compose.yml --project-directory . down

trust:
	$(COMPOSE) -f compose/docker-compose.yml --project-directory . run --rm bootstrap || true
	@echo "Also run host JWT steps if needed (see docs/compose-README.md)"

pins-propose:
	python3 release/propose-pins.py --pins pins.yaml --out pins.proposed.yaml --prefer-semver-tags

fetch-upstream:
	./scripts/fetch-upstream.sh
