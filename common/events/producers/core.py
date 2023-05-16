from celery import Celery

from kombu import Queue


def producer(context: dict, queue: Queue, app: Celery, producer=None) -> None:
    with app.producer_or_acquire(producer) as producer:
        producer.publish(
            context,
            serializer='json',
            exchange=queue.exchange,
            routing_key=str(queue.name),
            declare=[queue],
            retry=True,
        )
