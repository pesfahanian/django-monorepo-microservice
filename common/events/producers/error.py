from celery import Celery

from kombu import Queue

from common.events.producers.core import producer


def task_error_producer(task_name: str, task_kwargs: dict, app: Celery,
                        queue: Queue) -> None:
    producer(
        context={
            'task_name': task_name,
            'task_kwargs': task_kwargs,
        },
        queue=queue,
        app=app,
    )
