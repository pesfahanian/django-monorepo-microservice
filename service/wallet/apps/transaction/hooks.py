from common.grpc.clients.pg import perform_transaction_client
from common.models.choices import TransactionType


def perform_transaction_hook(user_id: str, amount: float,
                             type: TransactionType) -> None:
    perform_transaction_client(
        user_id=user_id,
        amount=amount,
        type=type,
    )
