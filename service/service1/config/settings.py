import sys

from pathlib import Path

from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

REPO_DIR = BASE_DIR.parent.parent

sys.path.append(str(REPO_DIR))

from common.config.settings import *

ADMIN_USERNAME = config(
    'ADMIN_USERNAME',
    default='admin',
)
ADMIN_PASSWORD = config(
    'ADMIN_PASSWORD',
    default='admin',
)

# * ----------------------------- Postgres -----------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config(
#             'DB_NAME',
#             default='dmm-service1',
#         ),
#         'USER': config(
#             'DB_USER',
#             default='postgres',
#         ),
#         'PASSWORD': config(
#             'DB_PASSWORD',
#             default='1234',
#         ),
#         'HOST': config(
#             'DB_HOST',
#             default='0.0.0.0',
#         ),
#         'PORT': config(
#             'DB_PORT',
#             default=5432,
#             cast=int,
#         ),
#     }
# }
# * --------------------------------------------------------------------

# * ------------------------------- API --------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

STATIC_URL = 'static/'

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
# * --------------------------------------------------------------------
