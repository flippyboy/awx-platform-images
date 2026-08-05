#!/usr/bin/env bash
# AWX web entrypoint: wait for DB, run migrations once, then start supervisord.
set -euo pipefail

if [ "$(id -u)" -ge 500 ]; then
    echo "awx:x:$(id -u):$(id -g):,,,:/var/lib/awx:/bin/bash" >> /tmp/passwd
    cat /tmp/passwd > /etc/passwd
    rm /tmp/passwd
fi

echo "[awx-web] Waiting for database..."
until awx-manage check --database default 2>/dev/null; do
    sleep 2
done
echo "[awx-web] Database is reachable."

if [ "${RUN_MIGRATIONS:-0}" = "1" ]; then
    echo "[awx-web] Running migrations..."
    awx-manage migrate --noinput
    echo "[awx-web] Migrations complete."

    ADMIN_USER="${DJANGO_SUPERUSER_USERNAME:-admin}"
    ADMIN_PASS="${DJANGO_SUPERUSER_PASSWORD:-admin}"
    ADMIN_EMAIL="${DJANGO_SUPERUSER_EMAIL:-admin@localhost}"

    if awx-manage createsuperuser --noinput \
        --username="$ADMIN_USER" \
        --email="$ADMIN_EMAIL" 2>/dev/null; then
        echo "[awx-web] Created superuser '$ADMIN_USER'"
    else
        echo "[awx-web] Superuser '$ADMIN_USER' already exists; ensuring password..."
    fi
    # Always set password so compose restarts with known credentials work
    awx-manage shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.filter(username='${ADMIN_USER}').first()
if u:
    u.set_password('${ADMIN_PASS}')
    u.is_superuser = True
    u.is_system_auditor = False
    u.save()
    print('Password updated for', u.username)
"

    # Register default execution environments if command exists
    awx-manage register_default_execution_environments 2>/dev/null || true
fi

echo "[awx-web] Starting supervisord (web)..."
exec supervisord -c /etc/supervisord_web.conf
