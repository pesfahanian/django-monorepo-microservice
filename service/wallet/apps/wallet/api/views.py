from django.db.models.query import QuerySet

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.wallet.api.serializers import WalletSerializer
from apps.wallet.models import Wallet


class GetWalletAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = WalletSerializer
    pagination_class = None

    queryset = Wallet.enabled_objects.all()

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).\
            filter(user_id=self.request.user.id)
