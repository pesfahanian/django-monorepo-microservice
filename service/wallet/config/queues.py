from kombu import Queue as _Queue

from common.events.queues import Queue
from common.events.utils import generate_queue

# TODO: Try absolute import here.
from .exchanges import ServiceExchange, ProducerExchange


class ServiceQueue:

    default = generate_queue(
        name=Queue.Wallet.default,
        exchange=ServiceExchange.default,
    )

    class Task:
        def _generate_queue(name: str) -> _Queue:
            return generate_queue(
                name=name,
                exchange=ServiceExchange.task,
            )

        entry_create = _generate_queue(Queue.Wallet.task_name('entry-create'))
        transaction_create = _generate_queue(
            Queue.Wallet.task_name('transaction-create'))

        _error = _generate_queue(Queue.Wallet.task_name('error'))


SERVICE_TASK_QUEUES = tuple(
    getattr(ServiceQueue.Task, attr) for attr in dir(ServiceQueue.Task)
    if not attr.startswith('_'))


class ProducerQueue:
    class Ledger:
        entry_create = generate_queue(
            name=Queue.Ledger.Consumer.entry_create,
            exchange=ProducerExchange.ledger,
        )
