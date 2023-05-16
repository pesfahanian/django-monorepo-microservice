from common.grpc.clients.pg import transaction_perform_client
from common.models.choices import TransactionType


def transaction_perform_hook(user_id: str, amount: float,
                             type: TransactionType) -> None:
    transaction_perform_client(
        user_id=user_id,
        amount=amount,
        type=type,
    )
