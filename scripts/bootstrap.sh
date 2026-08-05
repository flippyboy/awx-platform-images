#!/usr/bin/env bash
# Bootstrap: register Controller with Jewel + establish JWT trust.
# Runs as a one-shot compose service (python slim image — no curl).
set -euo pipefail

export JEWEL_URL="${JEWEL_URL:-https://jewel:8000}"
export CONTROLLER_HTTP="${CONTROLLER_HTTP:-http://controller-web:8052}"
export ADMIN_USER="${ADMIN_USER:-admin}"
export ADMIN_PASS="${ADMIN_PASS:-admin}"
export SECRET_OUT="${SECRET_OUT:-/secrets/controller_service_secret}"

python3 <<'PY'
import base64
import json
import os
import ssl
import subprocess
import time
import urllib.error
import urllib.request

JEWEL = os.environ["JEWEL_URL"].rstrip("/")
CONTROLLER = os.environ["CONTROLLER_HTTP"].rstrip("/")
USER = os.environ["ADMIN_USER"]
PASS = os.environ["ADMIN_PASS"]
SECRET_OUT = os.environ.get("SECRET_OUT", "/secrets/controller_service_secret")

ctx = ssl._create_unverified_context()
auth = base64.b64encode(f"{USER}:{PASS}".encode()).decode()


def http(method, url, data=None, authed=True, timeout=30):
    headers = {"Accept": "application/json"}
    if authed:
        headers["Authorization"] = f"Basic {auth}"
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            raw = resp.read().decode() or "{}"
            try:
                return resp.status, json.loads(raw)
            except json.JSONDecodeError:
                return resp.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read().decode() if e.fp else ""
        try:
            payload = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            payload = raw
        return e.code, payload
    except Exception as e:
        return 0, str(e)


def wait(url, name, attempts=90, authed=False):
    print(f"Waiting for {name} at {url} ...")
    for _ in range(attempts):
        code, _ = http("GET", url, authed=authed)
        if code in (200, 301, 302, 401, 403):
            print(f"{name} is up (HTTP {code}).")
            return
        time.sleep(5)
    raise SystemExit(f"ERROR: {name} did not become ready")


def list_results(path):
    code, body = http("GET", f"{JEWEL}{path}")
    if code != 200:
        print(f"  GET {path} -> {code}: {body}")
        return []
    if isinstance(body, dict):
        return body.get("results", [])
    if isinstance(body, list):
        return body
    return []


def find_by_name(path, name):
    for item in list_results(path):
        if item.get("name") == name:
            return item
    return None


def ensure(path, name, payload):
    existing = find_by_name(path, name)
    if existing:
        print(f"  exists {path} name={name} id={existing.get('id')}")
        return existing
    code, body = http("POST", f"{JEWEL}{path}", data=payload)
    if code in (200, 201) and isinstance(body, dict) and body.get("id"):
        print(f"  created {path} name={name} id={body['id']}")
        return body
    existing = find_by_name(path, name)
    if existing:
        print(f"  found after create {path} name={name} id={existing.get('id')} (HTTP {code})")
        return existing
    print(f"  FAILED create {path} name={name} HTTP {code}: {body}")
    return None


print("=== AWX Compose Bootstrap ===")
print(f"Jewel:      {JEWEL}")
print(f"Controller: {CONTROLLER}")

wait(f"{JEWEL}/api/", "Jewel API")
wait(f"{CONTROLLER}/api/v2/ping/", "Controller API")

code, api_root = http("GET", f"{JEWEL}/api/gateway/v1/")
print(f"Gateway API collections available: {sorted(api_root.keys()) if isinstance(api_root, dict) else api_root}")


def path_for(*candidates):
    if isinstance(api_root, dict):
        for c in candidates:
            key = c.strip("/").rstrip("/").split("/")[-1]
            if key in api_root:
                url = api_root[key]
                if url.startswith("http"):
                    return url.replace(JEWEL, "")
                return url
    return candidates[0]


PORTS = path_for("/api/gateway/v1/http_ports/")
TYPES = path_for("/api/gateway/v1/service_types/")
CLUSTERS = path_for("/api/gateway/v1/service_clusters/")
NODES = path_for("/api/gateway/v1/service_nodes/")
SERVICES = path_for("/api/gateway/v1/services/")

print("--- HTTP port ---")
port = ensure(
    PORTS,
    "API Port",
    {"name": "API Port", "number": 9080, "use_https": True, "is_api_port": True},
)

print("--- Service types ---")
for st in ("gateway", "controller"):
    t = find_by_name(TYPES, st)
    if not t:
        t = ensure(TYPES, st, {"name": st})
    else:
        print(f"  exists type {st} id={t.get('id')}")

gw_type = find_by_name(TYPES, "gateway")
ctrl_type = find_by_name(TYPES, "controller")
if not gw_type or not ctrl_type:
    raise SystemExit("Missing service types gateway/controller")

print("--- Service clusters ---")
gw_cluster = ensure(
    CLUSTERS,
    "gateway",
    {"name": "gateway", "service_type": gw_type["id"], "health_checks_enabled": True},
)
ctrl_cluster = ensure(
    CLUSTERS,
    "controller",
    {"name": "controller", "service_type": ctrl_type["id"], "health_checks_enabled": True},
)
if not gw_cluster or not ctrl_cluster:
    raise SystemExit("Failed to ensure service clusters")

print("--- Service nodes ---")
ensure(
    NODES,
    "Gateway Node 1",
    {"name": "Gateway Node 1", "service_cluster": gw_cluster["id"], "address": "jewel"},
)
ensure(
    NODES,
    "Controller Node",
    {
        "name": "Controller Node",
        "service_cluster": ctrl_cluster["id"],
        "address": "controller-web",
    },
)

print("--- Services (API routes) ---")
if port:
    ensure(
        SERVICES,
        "Gateway API",
        {
            "name": "Gateway API",
            "description": "Proxy to the gateway",
            "api_slug": "gateway",
            "http_port": port["id"],
            "service_cluster": gw_cluster["id"],
            "is_service_https": True,
            "service_path": "/",
            "service_port": 8000,
            "order": 100,
            "enable_gateway_auth": False,  # gateway must not JWT-auth itself
        },
    )
    ensure(
        SERVICES,
        "Controller API",
        {
            "name": "Controller API",
            "description": "Proxy to the Controller",
            "api_slug": "controller",
            "http_port": port["id"],
            "service_cluster": ctrl_cluster["id"],
            "is_service_https": True,
            "service_path": "/api/",
            "service_port": 8043,
            "order": 2,
            "enable_gateway_auth": True,  # inject JWT for Controller
        },
    )

print("--- JWT trust: link Controller ServiceID into Jewel ---")
# Best-effort: try to read install UUID / service id from controller via exec is done
# by the host Makefile when available. Here we only PATCH if CONTROLLER_SERVICE_ID is set.
sid = os.environ.get("CONTROLLER_SERVICE_ID", "").strip()
if sid:
    code, body = http(
        "PATCH",
        f"{JEWEL}{CLUSTERS}{ctrl_cluster['id']}/",
        data={"service_id": sid},
    )
    print(f"  PATCH service_id -> HTTP {code}: {body if code >= 400 else 'ok'}")
else:
    print("  CONTROLLER_SERVICE_ID not set; host-side setup will link it.")

print("--- JWT trust: ensure service secret exists ---")
# Secret is generated by host (`aap-gateway-manage generate_service_secret controller`)
# and mounted into Controller. If SECRET_OUT is writable and empty, note it.
if os.path.exists(SECRET_OUT):
    with open(SECRET_OUT) as f:
        secret = f.read().strip()
    if secret:
        print(f"  service secret present at {SECRET_OUT} (len={len(secret)})")
    else:
        print(f"  WARNING: {SECRET_OUT} is empty — run: make trust")
else:
    print(f"  WARNING: {SECRET_OUT} missing — run: make trust")

print("--- JWT public key reachable ---")
code, body = http("GET", f"{JEWEL}/api/gateway/v1/jwt_key/", authed=False)
if code == 200 and isinstance(body, str) and "BEGIN PUBLIC KEY" in body:
    print("  jwt_key OK")
elif code == 200:
    # might have been parsed wrong if content-type wrong
    print(f"  jwt_key HTTP 200 (payload type {type(body).__name__})")
else:
    print(f"  jwt_key HTTP {code}")

print("--- Controller via Jewel API index ---")
code, body = http("GET", f"{JEWEL}/api/", authed=False)
print(f"  /api/ -> {body}")

print()
print("=== Bootstrap complete ===")
print()
print("  USE THIS URL (Envoy — JWT injection works):")
print("    https://localhost")
print()
print("  Do NOT use https://localhost:8000 for the UI.")
print("  Port 8000 is Jewel only; /api/controller/* is not proxied there.")
print()
print(f"  Login: {USER} / {PASS}")
print()
print("  If Controller still returns 401 JWT errors, run on the host:")
print("    make trust")
print("    docker compose up -d --force-recreate controller-web controller-task")
PY
