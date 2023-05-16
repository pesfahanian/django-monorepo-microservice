from django_grpc.signals.wrapper import SignalWrapper

from proto import pg_pb2_grpc

from apps.pg.grpc.servicer import PGService


def register(server: SignalWrapper) -> None:
    pg_pb2_grpc.add_PGServiceServicer_to_server(
        PGService(),
        server,
    )
