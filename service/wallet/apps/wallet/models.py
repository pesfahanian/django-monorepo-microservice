import logging

from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import (
    TemporalModel,
    ToggleableModel,
    UUIDModel,
)

logger = logging.getLogger('django')


class Wallet(UUIDModel, ToggleableModel, TemporalModel):

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    user_id = models.UUIDField(
        _('User ID'),
        unique=True,
    )

    balance = models.DecimalField(
        default=0,
        max_digits=settings.DECIMAL_MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        validators=[
            MinValueValidator(0),
        ],
    )

    def deposit(self, amount: Decimal) -> None:
        logger.info(f'Depositing `{amount}` to user `{self.user_id}` wallet.')
        self.__class__.objects.filter(pk=self.pk).update(
            balance=models.F('balance') + amount)

    def withdraw(self, amount: Decimal) -> None:
        logger.info(
            f'Withdrawing `{amount}` from user `{self.user_id}` wallet.')
        updated_rows = self.__class__.objects.filter(
            pk=self.pk,
            balance__gte=amount,
        ).update(amount=models.F('balance') - amount)
        if (updated_rows == 0):
            raise ValueError(
                f'Insufficient funds in user `{self.user_id}` wallet.')

    def __str__(self) -> str:
        return str(self.user_id)
