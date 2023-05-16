from apps.core.tasks import task

from apps.ledger.handlers import entry_create_handler

from config.queues import ServiceQueue


@task(name=ServiceQueue.Task.entry_create.name,
      queue=ServiceQueue.Task.entry_create)
def entry_create_task(transaction_id: str) -> None:
    entry_create_handler(transaction_id=transaction_id)
