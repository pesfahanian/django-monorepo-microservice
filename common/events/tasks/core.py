from celery import Task as BaseTask

from common.config.settings import _CELERY_TASK_MAX_RETRIES
from common.events.producers.error import task_error_producer


class Task(BaseTask):
    app = None
    error_queue = None
    max_retries = _CELERY_TASK_MAX_RETRIES - 1

    # TODO: Add type-hinting here.
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if (self.request.retries >= self.max_retries):
            task_error_producer(
                task_name=self.__qualname__,
                task_kwargs=kwargs,
                app=self.app,
                queue=self.error_queue,
            )
        else:
            return super(Task, self).on_failure(
                exc,
                task_id,
                args,
                kwargs,
                einfo,
            )
