from django.db import transaction

from common.models.choices import TransactionType

from apps.ledger.tasks import entry_create_task

from apps.transaction.hooks import transaction_perform_hook
from apps.transaction.models import Transaction


def transaction_create_handler(transaction_id: str) -> None:
    try:
        with transaction.atomic():
            transaction_obj = Transaction.objects.get(id=transaction_id, )

            try:
                transaction_perform_hook(
                    user_id=str(transaction_obj.wallet.user_id),
                    amount=transaction_obj.amount,
                    type=transaction_obj.type,
                )
                
                transaction_obj.success()
                
                match transaction_obj.type:
                    case TransactionType.WITHDRAW:
                        transaction_obj.wallet.withdraw(amount=transaction_obj.amount)
                    case TransactionType.DEPOSIT:
                        transaction_obj.wallet.deposit(amount=transaction_obj.amount)
                    case _:
                        pass

                entry_create_task.delay(transaction_id=transaction_id)
            
            except:
                transaction_obj.fail()


    except Transaction.DoesNotExist:
        raise Exception(
            f'Transaction with ID `{transaction_id}` does not exist.')

    except Exception as e:
        raise e
