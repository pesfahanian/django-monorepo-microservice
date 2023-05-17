import logging

from apps.core.producers import producer

from config.queues import ProducerQueue

logger = logging.getLogger('django')


def entry_create_producer(transaction_id: str, user_id: str, amount: str,
                          type: int, created_at: str, updated_at: str) -> None:
    try:
        producer(
            context={
                'transaction_id': transaction_id,
                'user_id': user_id,
                'amount': amount,
                'type': type,
                'created_at': created_at,
                'updated_at': updated_at,
            },
            queue=ProducerQueue.Ledger.entry_create,
        )

    except Exception as e:
        logger.error('Failure in `entry_create_producer`. '
                     f'Reason: {str(e)}.')
