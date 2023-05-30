import logging

from apps.ledger.models import Entry

logger = logging.getLogger('django')


def entry_create_handler(**kwargs) -> None:
    try:
        Entry.objects.create(**kwargs)

    except Exception as e:
        logger.error('Failure in `entry_create_handler()`. '
                     f'Reason: {str(e)}.')
