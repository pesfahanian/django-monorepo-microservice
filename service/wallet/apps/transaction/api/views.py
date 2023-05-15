from django.db.models.query import QuerySet

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from common.models.choices import TransactionStatus

from apps.transaction.api.serializers import TransactionSerializer
from apps.transaction.models import Transaction


class TransactionListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer

    queryset = Transaction.objects.exclude(status=TransactionStatus.PENDING, )

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).\
            filter(wallet__user_id=self.request.user.id, )
