#!/usr/bin/env bash
# Jewel gateway entrypoint wrapper — ensures TLS certs and secret exist, then
# runs the stock launch-gateway script.
set -euo pipefail

GATEWAY_ETC=/etc/ansible-automation-platform/gateway
CERT="${GATEWAY_ETC}/gateway.crt"
KEY="${GATEWAY_ETC}/gateway.key"
SECRET="${GATEWAY_ETC}/SECRET_KEY"

# If certs were not mounted, generate ephemeral self-signed ones
if [ ! -s "$CERT" ] || [ ! -s "$KEY" ]; then
    echo "[jewel] Generating ephemeral TLS certificate..."
    openssl req -nodes -newkey rsa:2048 \
        -keyout "$KEY" -out /tmp/gateway.csr \
        -subj "/C=US/ST=NC/L=Durham/O=AWX-Compose/CN=localhost" 2>/dev/null
    openssl x509 -req -days 3650 -in /tmp/gateway.csr -signkey "$KEY" -out "$CERT" 2>/dev/null
    rm -f /tmp/gateway.csr
    chmod 644 "$CERT" "$KEY" 2>/dev/null || true
fi

if [ ! -s "$SECRET" ]; then
    echo "[jewel] Generating SECRET_KEY..."
    head -c 64 /dev/urandom | base64 | tr -d '\n' > "$SECRET"
    chmod 644 "$SECRET" 2>/dev/null || true
fi

# Ensure container-startup.yml is present for admin password bootstrap
STARTUP_SRC="${GATEWAY_STARTUP_FILE:-/opt/aap_gateway/src/container-startup.yml}"
if [ ! -f "$STARTUP_SRC" ] && [ -f /config/container-startup.yml ]; then
    mkdir -p /opt/aap_gateway/src
    cp /config/container-startup.yml /opt/aap_gateway/src/container-startup.yml
fi

export CONTAINER_NUMBER="${CONTAINER_NUMBER:-1}"
export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-aap_gateway_api.settings}"

echo "[jewel] Launching gateway (container ${CONTAINER_NUMBER})..."
exec /usr/bin/launch-gateway
