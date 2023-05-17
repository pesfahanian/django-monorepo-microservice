from apps.core.tasks import task

from config.queues import ServiceQueue


@task(name=ServiceQueue.Task.entry_create.name,
      queue=ServiceQueue.Task.entry_create)
def entry_create_task() -> None:
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
