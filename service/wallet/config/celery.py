from celery import Celery

from . import settings

app = Celery('dmm-wallet')

app.conf.update({
    'broker_url': settings.CELERY_BROKER_URL,
    'result_backend': settings.CELERY_RESULT_BACKEND,
    'accept_content': settings.CELERY_ACCEPT_CONTENT,
    'task_serializer': settings.CELERY_TASK_SERIALIZER,
    'result_serializer': settings.CELERY_RESULT_SERIALIZER,
    'task_ignore_results': settings.CELERY_TASK_IGNORE_RESULT,
    'timezone': settings.CELERY_TIMEZONE,
})

app.autodiscover_tasks(related_name='tasks')
app.autodiscover_tasks(related_name='producers')
