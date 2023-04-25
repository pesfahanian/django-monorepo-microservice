from datetime import timedelta
from pathlib import Path
import sys

from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

REPO_DIR = BASE_DIR.parent.parent

sys.path.append(str(REPO_DIR))

from common.config.settings import *

INSTALLED_APPS += [
    # * Apps
    'apps.core.apps.CoreConfig',

    # * Packages
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',

    # * Healthcheck
    'health_check',
    'health_check.db',
    'health_check.storage',
    'health_check.contrib.migrations',
]

MIDDLEWARE += [
    # * Packages
    'corsheaders.middleware.CorsMiddleware',
]

ADMIN_USERNAME = config(
    'ADMIN_USERNAME',
    default='admin',
)
ADMIN_PASSWORD = config(
    'ADMIN_PASSWORD',
    default='admin',
)

# * ----------------------------- Postgres -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config(
            'DB_NAME',
            default='dmm-wallet',
        ),
        'USER': config(
            'DB_USER',
            default='postgres',
        ),
        'PASSWORD': config(
            'DB_PASSWORD',
            default='1234',
        ),
        'HOST': config(
            'DB_HOST',
            default='0.0.0.0',
        ),
        'PORT': config(
            'DB_PORT',
            default=5432,
            cast=int,
        ),
    }
}
# * --------------------------------------------------------------------

# * ------------------------------- API --------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

STATIC_URL = 'static/'

STATIC_ROOT = 'static/'

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='*',
    cast=Csv(),
)

CORS_ORIGIN_ALLOW_ALL = config(
    'DEBUG',
    default=True,
    cast=bool,
)

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://0.0.0.0:8200',
    cast=Csv(),
)

CSRF_COOKIE_SECURE = config(
    'CSRF_COOKIE_SECURE',
    default=False,
    cast=bool,
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':
    timedelta(minutes=config(
        'ACCESS_TOKEN_LIFETIME',
        default=1440,
        cast=int,
    )),
    'REFRESH_TOKEN_LIFETIME':
    timedelta(days=config(
        'REFRESH_TOKEN_LIFETIME',
        default=16,
        cast=int,
    )),
    'ALGORITHM':
    'RS256',
    'VERIFYING_KEY':
    open('keys/jwtRS256.key.pub').read(),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_simplejwt.authentication.JWTTokenUserAuthentication', ),
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':
    10,
    'DATETIME_FORMAT':
    DATETIME_FORMAT,
    'DATE_FORMAT':
    DATE_FORMAT,
}
# * --------------------------------------------------------------------
