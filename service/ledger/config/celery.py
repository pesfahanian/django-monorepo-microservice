from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

REPO_DIR = BASE_DIR.parent.parent

sys.path.append(str(BASE_DIR))
sys.path.append(str(REPO_DIR))

import django

from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings',
)

django.setup()

app = Celery(
    'dmm-ledger',
    include=[
        'apps.core.tasks',
        'apps.ledger.consumers',
        'apps.ledger.tasks',
    ],
)

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY',
)

app.autodiscover_tasks(related_name='tasks')
app.autodiscover_tasks(related_name='consumers')
