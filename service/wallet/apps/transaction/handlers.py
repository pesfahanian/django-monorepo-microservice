from django.db import transaction

from common.models.choices import TransactionType, TransactionStatus

from apps.ledger.tasks import entry_create_task

from apps.transaction.hooks import transaction_perform_hook
from apps.transaction.models import Transaction

from apps.wallet.models import Wallet


def transaction_create_handler(transaction_id: str) -> None:
    try:
        with transaction.atomic():
            transaction_obj = Transaction.objects.select_for_update().get(
                id=transaction_id)
            wallet_obj = Wallet.objects.select_for_update().get(
                id=transaction_obj.wallet.id)

            if (transaction_obj.status == TransactionStatus.PENDING):
                raise ValueError('Transaction already resolved.')

            if (transaction_obj.type == TransactionType.WITHDRAW):
                wallet_obj.withdraw(amount=transaction_obj.amount)
            elif (transaction_obj.type == TransactionType.DEPOSIT):
                wallet_obj.deposit(amount=transaction_obj.amount)
            else:
                raise ValueError('Invalid transaction type.')

            transaction_obj.success()

            transaction.on_commit(
                lambda: entry_create_task.delay(transaction_id=transaction_id))

        transaction_perform_hook(
            user_id=str(wallet_obj.user_id),
            amount=transaction_obj.amount,
            type=transaction_obj.type,
        )

    except Transaction.DoesNotExist:
        raise Exception(
            f'Transaction with ID `{transaction_id}` does not exist.')

    except Exception as e:
        transaction_obj.fail()
        raise e
