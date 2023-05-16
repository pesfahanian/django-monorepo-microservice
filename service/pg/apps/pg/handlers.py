import logging

from common.models.choices import TransactionType

logger = logging.getLogger('django')


def transaction_perform_handler(user_id: str, amount: float,
                                type: TransactionType) -> None:
    # * Mock bank API.
    logger.info('---------------------------')
    logger.info(f'Transaction User ID: {user_id}')
    logger.info(f'Transaction Amount: {amount}')
    logger.info(f'Transaction Type: {type}')
    logger.info('---------------------------')
