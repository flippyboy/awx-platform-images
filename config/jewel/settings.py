# Jewel (gateway) settings overrides for docker-compose
import os

DEBUG = False
ALLOWED_HOSTS = ['*']

# Cookies: False so local HTTP debugging works; Envoy still terminates TLS
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Trust the compose hostnames
CSRF_TRUSTED_ORIGINS = [
    'https://localhost',
    'https://localhost:443',
    'https://localhost:8000',
    'https://127.0.0.1',
    'https://127.0.0.1:443',
    'https://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Frontend URL as seen by browsers
FRONT_END_URL = 'https://localhost'

# Envoy talks to gateway over HTTPS with self-signed certs
ENVOY_VERIFY_HTTPS_CERTIFICATES = False

# --- Redis over TCP (no TLS, no unix socket) for compose ---
_redis_url = os.environ.get('REDIS_URL', 'redis://redis-jewel:6379/0')
_redis_hosts = os.environ.get('REDIS_HOSTS', 'redis-jewel:6379')

CACHES = {
    'default': {
        'BACKEND': 'ansible_base.lib.cache.redis_cache.DABRedisCache',
        'LOCATION': _redis_url + '?db=4' if '?' not in _redis_url else _redis_url,
        'KEY_PREFIX': 'gateway',
    },
    'legacy': {
        'BACKEND': 'ansible_base.lib.cache.fallback_cache.DABCacheWithFallback',
    },
    'primary': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': _redis_url,
        'KEY_PREFIX': 'gateway',
        'OPTIONS': {
            'CLIENT_CLASS': 'ansible_base.lib.redis.RedisClient',
            'CLIENT_CLASS_KWARGS': {
                'mode': 'standalone',
                'redis_hosts': _redis_hosts,
                'ssl': False,
                'ssl_keyfile': None,
                'ssl_certfile': None,
                'ssl_cert_reqs': None,
                'ssl_ca_certs': None,
                'ssl_check_hostname': False,
                'socket_keepalive': True,
                'socket_timeout': 5,
                'socket_connect_timeout': 5,
                'cluster_error_retry_attempts': 0,
            },
        },
    },
    'fallback': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    },
}
