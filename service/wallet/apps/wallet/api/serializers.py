from django.conf import settings

from rest_framework import serializers

from common.api.serializers import TemporalModelSerializer

from apps.wallet.models import Wallet


class WalletSerializer(TemporalModelSerializer):
    balance = serializers.DecimalField(
        max_digits=settings.DECIMAL_MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )

    class Meta:
        model = Wallet
        fields = (
            'id',
            'balance',
        ) + TemporalModelSerializer.Meta.fields
