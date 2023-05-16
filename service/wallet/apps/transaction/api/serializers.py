from rest_framework import serializers

from common.api.serializers import TemporalModelSerializer
from common.models.choices import TransactionType

from apps.transaction.hooks import perform_transaction_hook
from apps.transaction.models import Transaction

from apps.wallet.models import Wallet


class TransactionSerializer(TemporalModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
            'user',
        ) + TemporalModelSerializer.Meta.fields

    def create(self, validated_data: dict) -> Transaction:
        user_id = validated_data['user'].id
        amount = validated_data['amount']
        type = validated_data['type']

        try:
            wallet_obj = Wallet.objects.get(user_id=user_id)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError(
                f'Wallet for user with ID `{user_id}` does not exist.')

        perform_transaction_hook(
            user_id=user_id,
            amount=amount,
            type=type,
        )

        transaction_obj = Transaction.objects.create(
            wallet=wallet_obj,
            amount=amount,
            type=type,
        )

        return transaction_obj
