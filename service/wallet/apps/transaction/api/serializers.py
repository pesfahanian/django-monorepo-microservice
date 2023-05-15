from rest_framework import serializers

from common.api.serializers import TemporalModelSerializer
from common.models.choices import TransactionType

from apps.transaction.models import Transaction


class TransactionSerializer(TemporalModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    id = serializers.UUIDField(read_only=True)
    status = serializers.IntegerField(read_only=True)

    amount = serializers.FloatField()
    type = serializers.ChoiceField(choices=TransactionType.choices)

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'type',
            'status',
            'user_id',
        ) + TemporalModelSerializer.Meta.fields

    def create(self, validated_data: dict) -> Transaction:
        pass
