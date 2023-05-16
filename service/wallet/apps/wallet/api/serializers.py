from common.api.serializers import TemporalModelSerializer

from apps.wallet.models import Wallet


class WalletSerializer(TemporalModelSerializer):

    # TODO: Balance should be a decimal field in response.
    class Meta:
        model = Wallet
        fields = (
            'id',
            'balance',
        ) + TemporalModelSerializer.Meta.fields
