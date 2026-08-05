# AWX Compose

A community-style **Docker Compose** packaging of the modern AWX stack from open-source components, without Red Hat product builds or the AWX Operator.

| Component | Upstream repo | Role in this stack |
|-----------|---------------|--------------------|
| **Controller** | [ansible/awx](https://github.com/ansible/awx) | Job scheduling & execution API (`ghcr.io/ansible/awx:devel` by default) |
| **Jewel** | [ansible/jewel](https://github.com/ansible/jewel) | Platform gateway (auth, service registry, Envoy xDS, optional UI hosting) |
| **Platform UI** | [ansible/ansible-ui](https://github.com/ansible/ansible-ui) (`platform/` workspace) | Browser UI (built here; not published as a public image) |

**Context (2025–2026):** Red Hat paused AWX product-style releases while refactoring into a pluggable architecture. Source is public; official multi-component compose releases and a public Platform UI image are not. See [AWX modernization: Moving forward](https://forum.ansible.com/t/awx-modernization-moving-forward/45134) and related posts below.

This repo is **glue only**: compose files, configs, Dockerfiles, patches, and scripts. Upstream trees under `controller/`, `ansible-ui/`, and `jewel/` are expected to stay **unmodified** checkouts.

**Operator / Helm (platform fork):** work under `operator/` and `charts/awx-platform-operator/` (fork of [awx-operator-helm](https://github.com/ansible-community/awx-operator-helm) with `AWXGateway` / `AWXPlatform`). See [docs/OPERATOR.md](docs/OPERATOR.md) and [charts/awx-platform-operator/README.md](charts/awx-platform-operator/README.md).

---

## Table of contents

1. [Architecture](#architecture)
2. [Prerequisites](#prerequisites)
3. [Quick start](#quick-start)
4. [Build pipeline (detailed)](#build-pipeline-detailed)
5. [All project modifications (inventory)](#all-project-modifications-inventory)
6. [Research & discoveries](#research--discoveries)
7. [JWT trust (Jewel ↔ Controller)](#jwt-trust-jewel--controller)
8. [Open license / subscription banner](#open-license--subscription-banner)
9. [Operations](#operations)
10. [Troubleshooting](#troubleshooting)
11. [Upstream references](#upstream-references)

---

## Architecture

### Request path (correct entrypoint)

```
Browser  ──HTTPS :443──►  Envoy
                            │  dynamic LDS/CDS from Jewel xDS (REST)
                            │
                            ├─ /                    static UI (via Jewel/nginx assets in routes)
                            ├─ /api/gateway/*       → Jewel :8000
                            └─ /api/controller/*    → Controller :8043
                                   │
                                   └─ Jewel gRPC ext_authz injects:
                                        X-DAB-JW-TOKEN + x-trusted-proxy
                                   Controller validates with ANSIBLE_BASE_JWT_KEY
```

### Ports

| URL | Service | Notes |
|-----|---------|--------|
| **https://localhost** (`ENVOY_PORT`, default **443**) | Envoy | **Use this for the UI** — only path with JWT injection to Controller |
| https://localhost:8000 | Jewel direct | Jewel API + UI static files; **`/api/controller/*` is NOT proxied** → UI shows Controller 404 |
| http://localhost:8052 | Controller HTTP | Debug / health; after `RESOURCE_SERVER` is set, many APIs are JWT-oriented |
| https://localhost:8043 | Controller HTTPS | Upstream for Envoy controller cluster |
| :19000 | Envoy admin | `curl http://localhost:19000/ready` |
| :5432 | Postgres | DBs: `awx`, `gateway` |
| :50051 | Jewel gRPC | Envoy control plane / ext_auth |

### Compose services

| Service | Image | Purpose |
|---------|-------|---------|
| `postgres` | `postgres:15` | Shared DB (`awx` + `gateway`) |
| `redis-awx` | `redis:7` | Controller broker/cache (TCP) |
| `redis-jewel` | `redis:7` | Jewel cache (TCP, no TLS in compose) |
| `controller-web` | `ghcr.io/ansible/awx:devel` | API + nginx + uwsgi + daphne |
| `controller-task` | same | Dispatcher / callback / wsrelay |
| `receptor` | `quay.io/ansible/receptor` | Local job mesh (`local-only` + control socket) |
| `jewel` | `awx-compose/jewel:local` | Gateway + Platform UI baked in |
| `envoy` | `envoyproxy/envoy` | Edge proxy; needs `envoy-path-rewrite.lua` |
| `bootstrap` | `python:3.12-slim` | One-shot: register services in Jewel |
| `platform-ui` | (profile `ui-standalone`) | Optional standalone UI on :4100 |

---

## Prerequisites

- Docker Engine
- Compose **v2** plugin **or** standalone `docker-compose` (Makefile auto-detects)
- ~8–12 GB RAM for Platform UI production build
- Free ports: 443, 8000, 8043, 8052 (override in `.env`)
- `openssl`, `make`, `curl` on the host for secrets / `make trust`

---

## Quick start

```bash
# 1. Clone upstream sources (if not already present)
git clone --depth 1 https://github.com/ansible/awx.git controller
git clone --depth 1 https://github.com/ansible/ansible-ui.git ansible-ui
git clone --depth 1 https://github.com/ansible/jewel.git jewel

# 2. Secrets + images
make secrets
make build              # platform-ui (with patches) + jewel-with-ui

# 3. Start stack (pulls awx:devel, postgres, redis, envoy, receptor, …)
make up

# 4. Wait until controller-web is healthy (first boot runs migrations), then:
make trust              # JWT: ServiceID link + service secret + controller restart

# 5. Open UI (accept self-signed cert)
#    https://localhost
#    Login: admin / admin
```

Override password via `ADMIN_PASSWORD` in `.env`.

---

## Build pipeline (detailed)

### Images this project builds

| Tag | Dockerfile | Inputs | Output |
|-----|------------|--------|--------|
| `awx-compose/platform-ui:local` | `docker/platform-ui/Dockerfile` | Clean `ansible-ui/` + `docker/platform-ui/patches/*.patch` | nginx image with `platform/dist` |
| `awx-compose/jewel:local` | `docker/jewel/Dockerfile` | `ghcr.io/ansible/jewel:latest` + platform-ui image | Jewel with UI under `/opt/aap_gateway/platform_ui` |
| `awx-compose/controller:local` (optional) | AWX `make Dockerfile HEADLESS=1` | `controller/` | Headless controller (UI not baked) |

### Platform UI build steps

1. Copy workspace `package.json` files; `npm ci --ignore-scripts`
2. Copy `framework`, `frontend`, `platform`, `locales`, …
3. **Apply patches** from `docker/platform-ui/patches/` (`patch -p1`)
4. `cd platform && npm run build` (Vite; relative API prefixes `/api/controller/v2`, etc.)
5. Copy `platform/dist` into nginx:1.27-alpine

Upstream `quay.io/ansible/platform-ui` is **not** public; baking the UI ourselves matches forum guidance (`HEADLESS=1` jewel builds + local UI).

### Jewel-with-UI build steps

1. `FROM ghcr.io/ansible/jewel:latest` (API-only GHCR image)
2. Replace placeholder `platform_ui` with assets from platform-ui image
3. Run as uid 1000 (same as upstream)

### Controller (default: pull, not build)

- Image: `ghcr.io/ansible/awx:devel`
- Config injected via mounts + `config/awx/settings.py` + entrypoints
- Optional: `make build-controller` then set `AWX_IMAGE=awx-compose/controller:local` in `.env`

### Make targets

| Target | Action |
|--------|--------|
| `make secrets` | TLS + Django secrets under `secrets/` |
| `make pull` | Pull base images |
| `make build-ui` | Build platform-ui only |
| `make build-jewel` / `make build` | UI + jewel-with-ui |
| `make build-controller` | Build controller from source (slow) |
| `make up` | `compose up -d --build` |
| `make trust` | JWT ServiceID + `generate_service_secret` + recreate controller |
| `make bootstrap` | Re-run service registration playbook-equivalent |
| `make down` / `make clean-volumes` | Stop / wipe volumes |
| `make logs` / `make ps` | Observe |

---

## All project modifications (inventory)

Nothing below should require commits **inside** `controller/`, `ansible-ui/`, or `jewel/` for normal operation.

### Root

| Path | Purpose |
|------|---------|
| `docker-compose.yml` | Full stack definition, env, volumes, healthchecks |
| `Makefile` | Build/up/trust orchestration; prefers `docker compose`, falls back to `docker-compose` |
| `.env` | Image tags, ports, credentials |
| `.dockerignore` | Keeps UI build context small (no `node_modules` / `.git`) |
| `.gitignore` | Local secrets/build artifacts |

### Config mounts

| Path | Purpose |
|------|---------|
| `config/awx/settings.py` | DB/Redis TCP; **JWT** (`ANSIBLE_BASE_JWT_KEY`, `RESOURCE_SERVER`); **open-license** monkeypatch for UI |
| `config/awx/nginx.conf` | Listen 8052/8043 → uwsgi/daphne (image default nginx is empty) |
| `config/awx/redis.conf` | TCP redis for multi-container (upstream defaults use unix socket) |
| `config/awx/receptor.conf` | `local-only` + control socket + local work type |
| `config/jewel/settings.py` | CSRF/cookies for compose; Redis TCP without TLS (upstream defaults TLS + unix socket) |
| `config/jewel/container-startup.yml` | Jewel admin username/password for launch-gateway |
| `config/envoy/envoy.yaml` | Static clusters to Jewel for REST xDS + gRPC |
| `config/envoy/envoy-path-rewrite.lua` | Copied from jewel; **required** or Envoy rejects LDS (`Invalid path: …lua`) |
| `config/postgres/init-databases.sh` | Creates `gateway` DB (`awx` is `POSTGRES_DB`) |

### Docker build

| Path | Purpose |
|------|---------|
| `docker/platform-ui/Dockerfile` | Multi-stage UI build + patch apply |
| `docker/platform-ui/nginx-default.conf` | SPA + long-cache assets on :8080 |
| `docker/platform-ui/patches/*.patch` | Compose-only UI fixes (see patches README) |
| `docker/platform-ui/patches/README.md` | How to add/regenerate patches |
| `docker/jewel/Dockerfile` | Jewel + UI bake |
| `docker/awx/Dockerfile` | Thin documentation wrapper around prebuilt/base controller |

### Scripts

| Path | Purpose |
|------|---------|
| `scripts/entrypoint-awx-web.sh` | Wait DB → migrate (once) → ensure superuser password → supervisord web |
| `scripts/entrypoint-awx-task.sh` | Wait migrations → `provision_instance` → supervisord task |
| `scripts/entrypoint-jewel.sh` | Ensure TLS/SECRET_KEY files → launch-gateway |
| `scripts/bootstrap.sh` | Register http_ports, clusters, nodes, services (PKs); notes JWT trust |

### Secrets (generated; not for production)

| File | Purpose |
|------|---------|
| `secrets/tls.crt` / `tls.key` | Shared self-signed TLS (Jewel + Controller nginx + Envoy mounts) |
| `secrets/awx_secret_key` | Django `SECRET_KEY` for Controller |
| `secrets/jewel_secret_key` | Jewel `SECRET_KEY` file |
| `secrets/controller_service_secret` | From `generate_service_secret controller`; Controller `RESOURCE_SERVER` |
| `secrets/controller_service_id` | Controller DAB `ServiceID`; linked onto Jewel service cluster |
| `secrets/jewel_jwt_public_key.pem` | Optional cache of Jewel JWT public key |
| `secrets/admin_*` | Local notes; runtime admin comes from `.env` / entrypoints |

---

## Research & discoveries

Findings from forum threads, source reading, and bring-up of this stack (2026).

### Product / community landscape

1. **No official “compose up the modern stack” release** — community repeatedly asked for jewel + UI + controller compose; RH focus is developer docs and source, not product artifacts for Jewel/UI.
2. **Three required pieces** after the refactor: Controller (awx), Platform UI (ansible-ui), Jewel (gateway). Old monolith UI was removed from awx (`HEADLESS` builds).
3. **Published images (partial):**
   - `ghcr.io/ansible/awx:devel` / `awx_devel` — exist
   - `ghcr.io/ansible/jewel:latest` — API-only, multi-arch, tracks `devel`
   - `quay.io/ansible/platform-ui` — **not public**
4. **Official dev paths** use each repo’s `make docker-compose*` (Ansible-templated compose), not a single integrated product compose.
5. Forum workarounds (e.g. Jon’s jewel patches) clone ansible-ui during jewel build — same idea as our multi-stage UI image.

### Technical discoveries (compose bring-up)

| Discovery | Implication for this repo |
|-----------|---------------------------|
| Controller **must** mount a real `nginx.conf` | Image default only has a stub on :80; we serve 8052/8043 |
| Controller Redis defaults are **unix socket** | Override `BROKER_URL` / `CACHES` / `CHANNEL_LAYERS` to TCP redis service |
| Jewel Redis defaults are **TLS + files + unix** | Override caches to non-TLS TCP in `config/jewel/settings.py` |
| Jewel `SECRET_KEY` must be a **file**, not only env | Mount `secrets/jewel_secret_key` |
| Dynaconf can leave `SECRET_KEY` empty if only file-as-bytes is used | Explicit string load in `config/awx/settings.py` |
| Postgres init: connecting as user `awx` without a DB fails | `POSTGRES_DB=awx`, create only `gateway` in init script |
| Receptor with only control-service may exit | Use `local-only: null` and run as root for socket permissions |
| Envoy LDS fails without lua file | Mount `envoy-path-rewrite.lua` at `/etc/envoy/envoy-path-rewrite.lua` |
| Jewel service APIs expect **integer PKs**, not names | Bootstrap lists then POSTs with IDs |
| Custom `/api/…` routes on API port are rejected | Use **services** with `api_slug` (e.g. `controller`), not free-form gateway_path under `/api/` |
| **JWT is mandatory for UI→Controller via gateway** | Without `ANSIBLE_BASE_JWT_KEY`, logs: `Failed to load cert from setting ANSIBLE_BASE_JWT_KEY` → HTTP 401 |
| JWT public key is at `GET /api/gateway/v1/jwt_key/` (PEM, no auth) | Set `ANSIBLE_BASE_JWT_KEY=https://jewel:8000` (URL form auto-appends jwt_key path) |
| `generate_service_secret controller` prints secret once | Store in `secrets/controller_service_secret`; set `RESOURCE_SERVER` |
| Link Controller `ServiceID` onto Jewel `ServiceCluster.service_id` | Required for resource-registry style trust |
| Setting `RESOURCE_SERVER__URL` can force JWT-only auth classes on Controller | Direct basic auth to Controller may stop working; UI path is via gateway |
| **Port 8000 cannot JWT-proxy Controller** | JWT injection is Envoy ext_authz → Jewel gRPC; browsers must use **:443** |
| Platform UI subscription banner is **AAP-oriented** | Open license omits `compliant`; UI treats missing as non-compliant → false “out of compliance” |
| OpenLicense in AWX is correct for OSS | Fix is UI awareness + optional `compliant: true` enrichment in settings |

### Upstream docs that matter

- Jewel: `docs/service_token_authentication.md` — service secret + `RESOURCE_SERVER`
- AWX: `tools/docker-compose/README.md` — devel compose (not this file)
- Forum series: Moving forward / Ansible UI / Ansible Jewel / Jewel on GHCR

---

## JWT trust (Jewel ↔ Controller)

### Failure mode

UI on https://localhost:

> HTTP 401: Error connecting to Controller API. This may indicate a misconfigured JWT key or service key…

Controller logs:

```text
Failed to validate x-trusted-proxy-header, unable to load cert
Failed to load cert from setting ANSIBLE_BASE_JWT_KEY
```

### What `make trust` does

1. Reads Controller DAB `ServiceID` via `awx-manage`
2. Sets Jewel `ServiceCluster(name=controller).service_id`
3. Runs `aap-gateway-manage generate_service_secret controller` → `secrets/controller_service_secret`
4. Recreates controller-web/task so settings pick up secret file + `ANSIBLE_BASE_JWT_KEY=https://jewel:8000`

### Settings (already in `config/awx/settings.py`)

- `ANSIBLE_BASE_JWT_KEY` — URL or PEM; URL recommended
- `ANSIBLE_BASE_JWT_VALIDATE_CERT = False` — compose self-signed TLS
- `RESOURCE_SERVER = { URL, SECRET_KEY, VALIDATE_HTTPS: False }` when secret file present

### Verify

```bash
# Gateway user → Controller via Envoy (JWT injected)
curl -sk -u admin:admin https://localhost/api/controller/v2/me/

# Public JWT key
curl -sk https://localhost:8000/api/gateway/v1/jwt_key/ | head
```

---

## Open license / subscription banner

### Should “Your subscription is out of compliance” show?

**No** for an upstream/open stack.

| Source | Behavior |
|--------|----------|
| Controller `/api/v2/config/` `license_info` | `license_type: "open"`, `product_name: "AWX"` — no RH subscription |
| Platform UI `PlatformApp.tsx` | Shows red banner if `!license_info.compliant` (AAP field) |

Missing `compliant` on open licenses made the UI look “non-compliant.”

### Mitigations in this repo

1. **Controller (immediate, no UI rebuild):** `config/awx/settings.py` replaces `OpenLicense.validate()` to return `compliant: True` and a large `time_remaining`.
2. **UI (build-time patch, clean upstream tree):**  
   `docker/platform-ui/patches/0001-skip-subscription-banner-for-open-license.patch`  
   skips banners when `license_type === 'open'`.

After controller restart, hard-refresh the browser. Rebuild jewel/UI when you want the patch inside the static assets:

```bash
make build-jewel && docker compose up -d --force-recreate jewel
```

---

## Operations

```bash
make logs
make ps
make bootstrap          # re-register Jewel services
make trust              # re-do JWT trust
make shell-awx
make shell-jewel
make down
make clean-volumes      # DESTROYS postgres data
```

### Updating upstream

```bash
# Keep trees clean — no local patches inside clones
(cd controller && git pull)
(cd ansible-ui && git pull)    # if UI patches fail, regenerate under docker/platform-ui/patches/
(cd jewel && git pull)         # only needed if you copy new lua/scripts from jewel

make build                     # if UI/jewel sources or patches changed
make up
make trust                     # if controller identity/secret rotated
```

### Env knobs (`.env`)

See `.env` for `AWX_IMAGE`, `JEWEL_*`, ports, `ADMIN_PASSWORD`, `DATABASE_*`.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| UI JWT 401 via :443 | No/expired JWT trust | `make trust`; check controller logs for `ANSIBLE_BASE_JWT_KEY` |
| UI Controller 404 via :8000 | Wrong entrypoint | Use **https://localhost** only |
| Envoy up but no listener / 000 | Missing lua rewrite script | Ensure `config/envoy/envoy-path-rewrite.lua` mounted |
| Controller stuck “Waiting for database” | SECRET_KEY empty / settings not loaded | Check mount of `settings.py` and `SECRET_KEY` file |
| Postgres exit on first boot | Init script connected to missing DB | Fixed via `POSTGRES_DB=awx` + gateway-only create |
| Receptor exits immediately | No `local-only` / socket perms | See `config/awx/receptor.conf`; receptor runs as root |
| Subscription red banner | AAP UI + open license | Controller open-license patch + UI patch (above) |
| `docker compose` unknown | No compose plugin | Install plugin or use `docker-compose` (Makefile detects) |
| Hub/EDA UI pages empty | Not in this compose | Expected; only controller service registered |

### Useful debug commands

```bash
docker compose ps -a
docker compose logs controller-web --tail=100
docker compose logs jewel --tail=50
docker compose logs envoy --tail=50
curl -sk https://localhost/api/controller/v2/ping/
curl -sk -u admin:admin https://localhost/api/gateway/v1/services/
curl -sf http://localhost:19000/config_dump | head   # Envoy admin
```

---

## Kubernetes / awx-operator (Option B)

See **[docs/OPERATOR.md](docs/OPERATOR.md)** for architecture findings and decisions.

| Path | Purpose |
|------|---------|
| `operator/awx-operator/` | Clone of awx-operator with Phase 1 gateway fields + CRD scaffolds |
| `deploy/kind/` | Kind cluster + CRDs + Jewel/Envoy smoke stack |
| `scripts/kind-up.sh` | Create kind cluster and apply smoke manifests |
| `scripts/kind-test.sh` | Validate CRDs + Jewel API |
| `scripts/kind-down.sh` | Delete kind cluster |

```bash
# Compose lab (optional)
make down

# Kind platform smoke
./scripts/kind-up.sh
./scripts/kind-test.sh

# Phase 2: run AWXGateway role (ansible) against kind — deploys demo-gateway*
python3 -m venv .venv-operator && .venv-operator/bin/pip install ansible kubernetes kubernetes
./scripts/kind-reconcile-gateway.sh
./scripts/kind-test.sh

./scripts/kind-down.sh   # when finished
```

## Upstream references

- [Blog: Upcoming Changes to the AWX Project](https://www.ansible.com/blog/upcoming-changes-to-the-awx-project/)
- [Streamlining AWX Releases](https://forum.ansible.com/t/streamlining-awx-releases/6894)
- [Refactoring AWX into a Pluggable Service-Oriented Architecture](https://forum.ansible.com/t/refactoring-awx-into-a-pluggable-service-oriented-architecture/7404)
- [AWX modernization: Moving forward](https://forum.ansible.com/t/awx-modernization-moving-forward/45134)
- [AWX modernization: Ansible UI](https://forum.ansible.com/t/awx-modernization-ansible-ui/45757)
- [AWX modernization: Ansible Jewel](https://forum.ansible.com/t/awx-modernization-ansible-jewel/45775)
- [Jewel container image on GHCR](https://forum.ansible.com/t/jewel-container-image-now-available-on-ghcr/46116)
- Jewel source: `docs/service_token_authentication.md`
- Packages: [ghcr.io/ansible/awx](https://github.com/ansible/awx/pkgs/container/awx), [ghcr.io/ansible/jewel](https://github.com/ansible/jewel/pkgs/container/jewel)

---

## License

Glue project files: **Apache-2.0**, aligned with upstream.  
`controller/`, `ansible-ui/`, and `jewel/` retain their own upstream licenses.

**Not production-supported.** Lab / developer packaging of evolving upstream `devel` artifacts.
