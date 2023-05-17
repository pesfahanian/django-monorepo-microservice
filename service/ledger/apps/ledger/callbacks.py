import logging

from apps.ledger.tasks import entry_create_task

logger = logging.getLogger('django')


def entry_create_callback(*args, **kwargs) -> None:
    try:
        # body = kwargs['body']
        entry_create_task.delay()

    except Exception as e:
        logger.error('Failure in `entry_create_callback()`. '
                     f'Reason: {str(e)}.')
