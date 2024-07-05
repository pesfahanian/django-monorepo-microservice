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
        self.__class__.objects.filter(pk=self.pk).update(
            status=TransactionStatus.SUCCESS)

    def fail(self) -> None:
        self.__class__.objects.filter(pk=self.pk).update(
            status=TransactionStatus.FAIL)

    def __str__(self) -> str:
        return f'{self.id}-{self.type}'
