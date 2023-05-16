import logging

from kombu import Queue

from common.events.decorators.tasks import task as _task

from config.celery import app
from config.queues import ServiceQueue

logger = logging.getLogger('django')


def task(queue: Queue, name: str):
    return _task(
        queue=queue,
        name=name,
        error_queue=ServiceQueue.Task._error,
        app=app,
        logger=logger,
    )
