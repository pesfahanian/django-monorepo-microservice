from apps.ledger.producers import entry_create_producer

from apps.transaction.models import Transaction


def entry_create_handler(transaction_id: str) -> None:
    try:
        transaction_obj = Transaction.objects.get(id=transaction_id, )

        entry_create_producer(
            transaction_id=transaction_id,
            user_id=str(transaction_obj.wallet.user_id),
            amount=str(transaction_obj.amount),
            type=transaction_obj.type,
            created_at=str(transaction_obj.created_at),
            updated_at=str(transaction_obj.updated_at),
        )

    except Transaction.DoesNotExist:
        raise Exception(
            f'Transaction with ID `{transaction_id}` does not exist.')

    except Exception as e:
        raise e
