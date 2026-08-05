#!/bin/bash
# Create the Jewel gateway database (awx DB is created via POSTGRES_DB)
set -euo pipefail

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT 'CREATE DATABASE gateway'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'gateway')\gexec
EOSQL

echo "Database gateway is ready (awx already exists as POSTGRES_DB)."
