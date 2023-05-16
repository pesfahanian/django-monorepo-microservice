from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TemporalModel, UUIDModel
from common.models.choices import TransactionStatus, TransactionType


class Transaction(UUIDModel, TemporalModel):

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    wallet = models.ForeignKey(
        'wallet.Wallet',
        on_delete=models.CASCADE,
        related_name='transactions',
    )

    amount = models.DecimalField(
        max_digits=settings.DECIMAL_MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        validators=[
            MinValueValidator(0),
        ],
    )

    type = models.PositiveSmallIntegerField(
        _('Type'),
        choices=TransactionType.choices,
    )
    status = models.PositiveSmallIntegerField(
        _('Type'),
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
    )

    def success(self) -> None:
        self.status = TransactionStatus.SUCCESS
        self.save()

    def fail(self) -> None:
        self.status = TransactionStatus.FAIL
        self.save()

    def __str__(self) -> str:
        return f'{self.id}-{self.type}'
