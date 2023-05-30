from __future__ import absolute_import, unicode_literals

import logging

import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

REPO_DIR = BASE_DIR.parent.parent

sys.path.append(str(BASE_DIR))
sys.path.append(str(REPO_DIR))

import django

from celery import Celery

from kombu import Queue

from common.events.consumers import AMQPConsumer
from common.events.decorators.tasks import task as _task

logger = logging.getLogger('django')

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings',
)

app = Celery('dmm-ledger', )

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY',
)

django.setup()

from apps.ledger.handlers import entry_create_handler

# TODO: Try absolute import here.
from .queues import ServiceQueue


# ! Hacky fix since consumer in the app didn't work.
def task(queue: Queue, name: str):
    return _task(
        queue=queue,
        name=name,
        error_queue=ServiceQueue.Task._error,
        app=app,
        logger=logger,
    )


@task(name=ServiceQueue.Task.entry_create.name,
      queue=ServiceQueue.Task.entry_create)
def entry_create_task(**kwargs) -> None:
    entry_create_handler(**kwargs)


def entry_create_callback(*args, **kwargs) -> None:
    try:
        entry_create_task.delay(**kwargs['body'])

    except Exception as e:
        logger.error('Failure in `entry_create_callback()`. '
                     f'Reason: {str(e)}.')


class EntryCreateConsumer(AMQPConsumer):
    queue = ServiceQueue.Consumer.entry_create
    callback = entry_create_callback
    logger = logger


app.steps['consumer'].add(EntryCreateConsumer)
