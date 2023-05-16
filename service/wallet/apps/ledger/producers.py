import logging

from apps.core.producers import producer

from config.queues import ProducerQueue

logger = logging.getLogger('uvicorn')


def entry_create_producer(context: dict) -> None:
    try:
        producer(
            context=context,
            queue=ProducerQueue.Ledger.entry_create,
        )

    except Exception as e:
        logger.error('Failure in `entry_create_producer`. '
                     f'Reason: {str(e)}.')
