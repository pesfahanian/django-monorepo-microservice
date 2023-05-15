from common.api.serializers import TemporalModelSerializer

from apps.wallet.models import Wallet


class WalletSerializer(TemporalModelSerializer):

    class Meta:
        model = Wallet
        fields = (
            'id',
            'balance',
        ) + TemporalModelSerializer.Meta.fields
