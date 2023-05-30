from logging import Logger

from functools import wraps
from typing import Callable

from celery import Celery

from kombu import Queue

from common.config.settings import _CELERY_TASK_MAX_RETRIES
from common.events.tasks import Task


# TODO: Add type-hinting here.
def task(queue: Queue, name: str, error_queue: Queue, app: Celery,
         logger: Logger):
    def decorator(func: Callable):
        @app.task(base=Task,
                  app=app,
                  name=name,
                  queue=queue,
                  error_queue=error_queue,
                  autoretry_for=(Exception, ),
                  retry_backoff=_CELERY_TASK_MAX_RETRIES)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f'Failure in `{func.__name__}()`. '
                             f'Reason: {str(e)}.')
                raise e

        return wrapper

    return decorator
