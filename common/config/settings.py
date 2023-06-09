from decouple import config

from common.config.logger import CustomFormat, CustomFilter

SECRET_KEY = config(
    'SECRET_KEY',
    default=  # noqa
    r'django-insecure-6ognx_g8i3=x-7op@d$x@26qh_n*308#t&s5zy&!fs526+m3rs',
)

DEBUG = config(
    'DEBUG',
    default=True,
    cast=bool,
)

INSTALLED_APPS = [
    # * Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # * Default
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

DATETIME_INPUT_FORMAT = '%Y-%m-%d %H:%M:%S'

DATE_FORMAT = '%Y-%m-%d'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': CustomFormat,
            'format': '[{asctime}] {levelname} | ({module}) {message}',
            'style': '{',
        },
    },
    'filters': {
        'custom_filter': {
            '()': CustomFilter,
        }
    },
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['custom_filter'],
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    },
}

DECIMAL_MAX_DIGITS = 14

DECIMAL_PLACES = 4

# * ------------------------------- API --------------------------------
PAGE_SIZE = config(
    'PAGE_SIZE',
    default=10,
    cast=int,
)
# * --------------------------------------------------------------------

# * ------------------------------- gRPC -------------------------------
PG_SERVICE_GRPC_HOST = config(
    'PG_SERVICE_GRPC_HOST',
    default='0.0.0.0',
)
PG_SERVICE_GRPC_PORT = config(
    'PG_SERVICE_GRPC_PORT',
    default=50150,
    cast=int,
)
PG_SERVICE_GRPC_URL = f'{PG_SERVICE_GRPC_HOST}:{PG_SERVICE_GRPC_PORT}'
# * --------------------------------------------------------------------

# * ------------------------------ Celery ------------------------------
_CELERY_TASK_MAX_RETRIES = 3
# * --------------------------------------------------------------------
