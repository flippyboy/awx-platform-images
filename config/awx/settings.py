# AWX settings for docker-compose deployment
import os
import socket

# Explicit SECRET_KEY (file-based load can end up empty under dynaconf + bytes)
_secret_path = os.environ.get('AWX_SECRET_KEY_FILE', '/etc/tower/SECRET_KEY')
if os.path.exists(_secret_path):
    with open(_secret_path, 'r', encoding='utf-8') as _f:
        SECRET_KEY = _f.read().strip()
else:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'insecure-compose-dev-key-change-me')

ADMINS = ()
STATIC_ROOT = '/var/lib/awx/public/static'
STATIC_URL = '/static/'
PROJECTS_ROOT = '/var/lib/awx/projects'
JOBOUTPUT_ROOT = '/var/lib/awx/job_status'

# Docker (not Kubernetes) execution
IS_K8S = False
AWX_PROOT_ENABLED = False
AWX_AUTO_DEPROVISION_INSTANCES = True

CLUSTER_HOST_ID = socket.gethostname()
SYSTEM_UUID = os.environ.get('SYSTEM_UUID', '00000000-0000-0000-0000-000000000001')

ALLOWED_HOSTS = ['*']
INTERNAL_API_URL = 'http://127.0.0.1:8052'

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
USE_X_FORWARDED_PORT = True
USE_X_FORWARDED_HOST = True

BROADCAST_WEBSOCKET_PORT = 8052
BROADCAST_WEBSOCKET_PROTOCOL = 'http'
BROADCAST_WEBSOCKET_VERIFY_CERT = False

# Database
DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'awx.main.db.profiled_pg',
        'NAME': os.environ.get('DATABASE_NAME', 'awx'),
        'USER': os.environ.get('DATABASE_USER', 'awx'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'awx'),
        'HOST': os.environ.get('DATABASE_HOST', 'postgres'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

# Redis over TCP (shared redis service)
_redis_host = os.environ.get('REDIS_HOST', 'redis-awx')
_redis_port = os.environ.get('REDIS_PORT', '6379')
BROKER_URL = f'redis://{_redis_host}:{_redis_port}/0'
CACHES = {
    'default': {
        'BACKEND': 'ansible_base.lib.cache.redis_cache.DABRedisCache',
        'LOCATION': f'redis://{_redis_host}:{_redis_port}/1',
    }
}
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [BROKER_URL],
            'capacity': 10000,
            'group_expiry': 157784760,
        },
    }
}

# Receptor
RECEPTORCTL_SOCKET = os.environ.get('RECEPTORCTL_SOCKET', '/var/run/receptor/receptor.sock')

# Logging to stdout for containers
AWX_LOGGING_MODE = 'stdout'

# ---------------------------------------------------------------------------
# Jewel / Platform Gateway trust
#
# Gateway injects X-DAB-JW-TOKEN + x-trusted-proxy when proxying to Controller.
# Controller validates those using Jewel's JWT public key.
# ---------------------------------------------------------------------------

# URL base of Jewel — JWTCert fetches {URL}/api/gateway/v1/jwt_key/
# Can also be a PEM string or file:// path.
_jwt_key = os.environ.get('ANSIBLE_BASE_JWT_KEY', 'https://jewel:8000')
ANSIBLE_BASE_JWT_KEY = _jwt_key
ANSIBLE_BASE_JWT_VALIDATE_CERT = False  # self-signed TLS in compose

# Shared secret so Controller can call Jewel (resource registry, claims, etc.)
_resource_url = os.environ.get('RESOURCE_SERVER_URL', 'https://jewel:8000')
_resource_secret = os.environ.get('RESOURCE_SERVER_SECRET_KEY', '')
# Allow secret from mounted file (bootstrap writes this)
_secret_file = os.environ.get(
    'RESOURCE_SERVER_SECRET_KEY_FILE',
    '/etc/tower/conf.d/controller_service_secret',
)
if not _resource_secret and os.path.exists(_secret_file):
    with open(_secret_file, 'r', encoding='utf-8') as _f:
        _resource_secret = _f.read().strip()

if _resource_url and _resource_secret:
    RESOURCE_SERVER = {
        'URL': _resource_url,
        'SECRET_KEY': _resource_secret,
        'VALIDATE_HTTPS': False,
    }

# ---------------------------------------------------------------------------
# Open-source license presentation for Platform UI
#
# AWX's OpenLicense intentionally omits AAP subscription fields. The Platform UI
# (ansible-ui) was written for AAP and shows "subscription is out of compliance"
# whenever license_info.compliant is missing/false. For upstream/open installs
# that banner is noise — mark open licenses as compliant.
# ---------------------------------------------------------------------------
try:
    from awx.main.utils import licensing as _awx_licensing

    class _OpenLicenseCompliant:  # noqa: N801
        def validate(self):
            return {
                'license_type': 'open',
                'valid_key': True,
                'subscription_name': 'OPEN',
                'product_name': 'AWX',
                'compliant': True,
                'date_expired': False,
                'date_warning': False,
                # Far-future so the UI "expires in N days" banner never fires
                'time_remaining': 60 * 60 * 24 * 365 * 100,
                'grace_period_remaining': 0,
                'free_instances': 9999999,
                'instance_count': 9999999,
            }

    _awx_licensing.OpenLicense = _OpenLicenseCompliant
except Exception:
    pass

