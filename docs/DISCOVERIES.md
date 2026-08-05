# Discoveries log

Longer-form notes from designing and bringing up this compose stack.  
Operational summary lives in [README.md](../README.md); this file is the research trail.

Related: [OPERATOR.md](OPERATOR.md) (Option B / awx-operator), AAP uses the same Envoy multi-service front-door as this compose stack.

## Why this repo exists

Red Hat’s AWX modernization split the old “AWX image with UI” story into:

1. **Controller** — `ansible/awx` (job engine / API)
2. **Jewel** — `ansible/jewel` (platform gateway; open-sourced later)
3. **Platform UI** — `ansible/ansible-ui` `platform/` app

Official posture (forum 2026): source + some **devel** images; **no** versioned Jewel/UI product releases or public Platform UI image. Community requests for a “just compose up” stack are exactly what this repository implements.

## Image availability (as of bring-up)

| Artifact | Available? | Notes |
|----------|------------|--------|
| `ghcr.io/ansible/awx:devel` | Yes | Production-style controller image used here |
| `ghcr.io/ansible/awx_devel:devel` | Yes | Source-mounted devel image (not used as default) |
| `ghcr.io/ansible/jewel:latest` | Yes | API-only; multi-arch; tracks devel |
| `quay.io/ansible/platform-ui` | No (auth) | Jewel Dockerfiles still reference it for non-headless builds |
| Operator install of “modern” stack | Incomplete for community | Jewel not wired like full AAP |

## Architecture decisions we made

### Envoy is the real front door

Jewel’s nginx serves UI + gateway API on :8000. Controller routing for browsers is **not** done there. Envoy:

- Loads dynamic listeners/clusters from Jewel’s REST xDS
- Calls Jewel gRPC external auth to inject JWT toward Controller
- Needs `envoy-path-rewrite.lua` or LDS apply fails with `Invalid path: /etc/envoy/envoy-path-rewrite.lua`

**Rule:** Use `https://localhost` (Envoy). Do not use `:8000` as the UI origin if you need Controller.

### Prefer prebuilt controller; build UI + jewel-with-UI

Building controller from source (`make Dockerfile` / `awx-kube-build`) is heavy and Ansible-templated. GHCR `awx:devel` is enough if we mount nginx + settings + entrypoints.

UI must be built: no public image. Jewel GHCR is API-only; we layer UI assets.

### Keep upstream git trees clean

All compose-specific behavior lives in:

- `config/`
- `docker/` (including `platform-ui/patches/`)
- `scripts/`
- `docker-compose.yml` / `Makefile`

Patches to ansible-ui are applied **only in the Docker build**, so `git pull` in `ansible-ui/` stays easy.

## Failure modes we hit (and fixes)

### 1. Postgres init exit

**Error:** `FATAL: database "awx" does not exist` during init scripts when `POSTGRES_USER=awx` and default DB was `postgres`.

**Fix:** `POSTGRES_DB=awx`; init script only ensures `gateway` exists.

### 2. Controller SECRET_KEY empty

**Error:** `ImproperlyConfigured: The SECRET_KEY setting must not be empty` despite a non-empty secret file.

**Fix:** Explicit UTF-8 string read in `config/awx/settings.py` (dynaconf/bytes interaction with file-based defaults was unreliable).

### 3. Redis assumptions

AWX defaults: `unix:///var/run/redis/redis.sock`.  
Jewel defaults: TLS redis with cert paths + unix default cache.

**Fix:** TCP Redis services + full cache/broker overrides in settings.

### 4. Receptor exit

**Error:** `Nothing to do - no backends` / socket lock permission denied.

**Fix:** `local-only` in receptor.conf; run receptor as root; shared volume for socket.

### 5. JWT 401 in UI

**Error:** Platform UI “misconfigured JWT key or service key”; controller logs missing `ANSIBLE_BASE_JWT_KEY`.

**Fix:**

- `ANSIBLE_BASE_JWT_KEY=https://jewel:8000` (fetches `/api/gateway/v1/jwt_key/`)
- `ANSIBLE_BASE_JWT_VALIDATE_CERT=False`
- `RESOURCE_SERVER` with secret from `generate_service_secret controller`
- Set Jewel controller cluster `service_id` to Controller’s DAB ServiceID  
  Automated by `make trust`.

### 6. Subscription compliance banner on open source

**Observation:** Controller correctly returns open license; UI still shows “out of compliance”.

**Root cause:** AAP Platform UI checks `license_info.compliant`. OpenLicense does not set that field → falsy → banner.

**Fix:**

- Settings monkeypatch: open license returns `compliant: true`
- UI patch at build: skip banners when `license_type === 'open'`

### 7. Bootstrap API shape

Jewel REST modules expect primary keys for FKs (`service_type`, `http_port`, `service_cluster`).  
Posting names returns 400 `Expected pk value, received str`.

Gateway path routes under `/api/` on the API port are rejected; use **services** with `api_slug`.

## What is intentionally incomplete

- **Hub / EDA / Lightspeed** — not registered; UI sections may 404 or look empty
- **Full job execution E2E** — receptor present; EE pull / execution not hardened as a product install
- **SSO / LDAP** — django-ansible-base plugins exist upstream; not wired in this compose
- **Production TLS / HA / backups** — lab only
- **Automatic trust on first boot** — bootstrap registers services; `make trust` still required once controller has a stable ServiceID (could be merged later)

## Forum / source breadcrumbs

- Moving forward + community asking for compose: [thread](https://forum.ansible.com/t/awx-modernization-moving-forward/45134) (esp. later pages)
- UI quickstart (separate awx compose + `npm start`): [Ansible UI](https://forum.ansible.com/t/awx-modernization-ansible-ui/45757)
- Jewel quickstart + HEADLESS: [Ansible Jewel](https://forum.ansible.com/t/awx-modernization-ansible-jewel/45775)
- GHCR jewel: [announcement](https://forum.ansible.com/t/jewel-container-image-now-available-on-ghcr/46116)
- Jewel `docs/service_token_authentication.md` in jewel clone
- AWX `awx/main/utils/licensing.py` — `OpenLicense`
- ansible-ui `platform/main/PlatformApp.tsx` — subscription banners
- ansible-base `jwt_consumer.common.cert.JWTCert` — URL vs PEM for `ANSIBLE_BASE_JWT_KEY`
