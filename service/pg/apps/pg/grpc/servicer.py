import logging

from google.protobuf import empty_pb2

import grpc
from grpc._server import _Context

from proto import pg_pb2, pg_pb2_grpc

from apps.pg.handlers import transaction_perform_handler

logger = logging.getLogger('django')


class PGService(pg_pb2_grpc.PGServiceServicer):

    def TransactionPerform(self, request: pg_pb2.TransactionPerformRequest,
                           context: _Context) -> empty_pb2.Empty:
        try:
            transaction_perform_handler(
                user_id=request.userID,
                amount=request.amount,
                type=request.type,
            )

            return empty_pb2.Empty()

        except Exception as e:
            details = ('Failure in `PGService.TransactionPerform()`. '
                       f'Reason: {str(e)}.')
            logger.error(details)
            context.abort(
                code=grpc.StatusCode.INTERNAL,
                details=details,
            )
