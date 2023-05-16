from apps.core.tasks import task

from apps.transaction.handlers import transaction_create_handler

from config.queues import ServiceQueue


@task(name=ServiceQueue.Task.transaction_create.name,
      queue=ServiceQueue.Task.transaction_create)
def transaction_create_task(transaction_id: str) -> None:
    transaction_create_handler(transaction_id=transaction_id)
