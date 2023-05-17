from pathlib import Path
import sys

from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

REPO_DIR = BASE_DIR.parent.parent

sys.path.append(str(REPO_DIR))

from common.config.settings import *

# TODO: Try absolute imports here.
from .exchanges import ServiceExchange
from .queues import ServiceQueue, SERVICE_TASK_QUEUES

INSTALLED_APPS += [
    # * Apps
    'apps.core.apps.CoreConfig',
    'apps.ledger.apps.LedgerConfig',

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

DECIMAL_MAX_DIGITS = 14

DECIMAL_PLACES = 4

# * ----------------------------- Postgres -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config(
            'DB_NAME',
            default='dmm-ledger',
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
    'CORS_ORIGIN_ALLOW_ALL',
    default=True,
    cast=bool,
)

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://0.0.0.0:8201',
    cast=Csv(),
)

CSRF_COOKIE_SECURE = config(
    'CSRF_COOKIE_SECURE',
    default=False,
    cast=bool,
)
# * --------------------------------------------------------------------

# * ----------------------------- RabbitMQ -----------------------------
RABBITMQ_USER = config(
    'RABBITMQ_USER',
    default='guest',
)
RABBITMQ_PASSWORD = config(
    'RABBITMQ_PASSWORD',
    default='guest',
)
RABBITMQ_HOST = config(
    'RABBITMQ_HOST',
    default='0.0.0.0',
)
RABBITMQ_PORT = config(
    'RABBITMQ_PORT',
    default=5672,
    cast=int,
)
RABBITMQ_DSN = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//'
# * --------------------------------------------------------------------

# * ------------------------------ Celery ------------------------------
CELERY_BROKER_URL = RABBITMQ_DSN
CELERY_RESULT_BACKEND = None
CELERY_ACCEPT_CONTENT = [
    'application/json',
]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_IGNORE_RESULT = True
CELERY_DEFAULT_QUEUE = str(ServiceQueue.default.name)
CELERY_DEFAULT_EXCHANGE = str(ServiceExchange.default.name)
CELERY_DEFAULT_ROUTING_KEY = str(ServiceQueue.default.name)
CELERY_TASK_QUEUES = (ServiceQueue.default, ) + SERVICE_TASK_QUEUES
# * --------------------------------------------------------------------
