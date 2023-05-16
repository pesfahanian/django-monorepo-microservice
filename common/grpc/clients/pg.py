import logging

import grpc

from common.config import settings
from common.models.choices import TransactionType

from proto import pg_pb2, pg_pb2_grpc

logger = logging.getLogger('django')

logger.info(f'{settings.PG_SERVICE_GRPC_URL = }')


def perform_transaction_client(user_id: str, amount: float,
                               type: TransactionType) -> None:
    try:
        with grpc.insecure_channel(settings.PG_SERVICE_GRPC_URL) as channel:
            stub = pg_pb2_grpc.PGServiceStub(channel)
            stub.PerformTransaction(
                pg_pb2.PerformTransactionRequest(
                    userID=user_id,
                    amount=amount,
                    type=type,
                ), )

    except grpc.RpcError as rpc_error:
        details = rpc_error.details()
        logger.error('Failure in `perform_transaction_client()`. '
                     f'Reason: {details}.')
        raise Exception(details)
