from kombu import Queue

from common.events.producers import producer as _producer

from config.celery import app


def producer(context: dict, queue: Queue) -> None:
    return _producer(
        context=context,
        queue=queue,
        app=app,
    )
