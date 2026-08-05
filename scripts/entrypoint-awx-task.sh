#!/usr/bin/env bash
# AWX task entrypoint: wait for migrations, provision instance, start workers.
set -euo pipefail

if [ "$(id -u)" -ge 500 ]; then
    echo "awx:x:$(id -u):$(id -g):,,,:/var/lib/awx:/bin/bash" >> /tmp/passwd
    cat /tmp/passwd > /etc/passwd
    rm /tmp/passwd
fi

echo "[awx-task] Waiting for migrations..."
if command -v wait-for-migrations >/dev/null 2>&1; then
    wait-for-migrations
else
    until awx-manage check --database default 2>/dev/null; do sleep 2; done
    until ! awx-manage showmigrations 2>/dev/null | grep -q '\[ \]'; do sleep 2; done
fi
echo "[awx-task] Migrations ready."

echo "[awx-task] Provisioning instance..."
awx-manage provision_instance --hostname="$(hostname)" --node_type=hybrid 2>/dev/null \
  || awx-manage provision_instance 2>/dev/null \
  || true

echo "[awx-task] Starting supervisord (task)..."
exec supervisord -c /etc/supervisord_task.conf
