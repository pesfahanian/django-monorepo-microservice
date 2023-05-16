from kombu import Queue

from common.events.queues import Queue
from common.events.utils import generate_queue

from .exchanges import ServiceExchange


class ServiceQueue:

    default = generate_queue(
        name=Queue.Wallet.default,
        exchange=ServiceExchange.default,
    )

    class Task:

        def _generate_queue(name: str) -> Queue:
            return generate_queue(
                name=name,
                exchange=ServiceExchange.task,
            )

        transaction_create = _generate_queue(
            Queue.Wallet.task_name('transaction-create'))

        _error = _generate_queue(Queue.Wallet.task_name('error'))


SERVICE_TASK_QUEUES = tuple(
    getattr(ServiceQueue.Task, attr) for attr in dir(ServiceQueue.Task)
    if not attr.startswith('_'))
