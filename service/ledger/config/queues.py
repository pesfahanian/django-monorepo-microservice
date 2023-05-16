from kombu import Queue as _Queue

from common.events.queues import Queue
from common.events.utils import generate_queue

# TODO: Try absolute import here.
from .exchanges import ServiceExchange


class ServiceQueue:

    default = generate_queue(
        name=Queue.Ledger.default,
        exchange=ServiceExchange.default,
    )

    class Task:

        def _generate_queue(name: str) -> _Queue:
            return generate_queue(
                name=name,
                exchange=ServiceExchange.task,
            )

        entry_create = _generate_queue(Queue.Ledger.task_name('entry-create'))

        _error = _generate_queue(Queue.Ledger.task_name('error'))

    class Consumer:

        def _generate_queue(name: str) -> _Queue:
            return generate_queue(
                name=name,
                exchange=ServiceExchange.consumer,
            )

        entry_create = _generate_queue(Queue.Ledger.Consumer.entry_create)


SERVICE_TASK_QUEUES = tuple(
    getattr(ServiceQueue.Task, attr) for attr in dir(ServiceQueue.Task)
    if not attr.startswith('_'))
