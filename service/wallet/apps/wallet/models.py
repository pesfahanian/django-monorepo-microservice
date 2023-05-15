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
        self.balance += amount
        self.save()
        # TODO: Ledger producer background task here.

    def withdraw(self, amount: Decimal) -> None:
        logger.info(
            f'Withdrawing `{amount}` from user `{self.user_id}` wallet.')
        if (amount > self.balance):
            raise ValueError(
                f'Insufficient amount in user `{self.user_id}` wallet')
        self.locked = self.locked - amount
        self.save()
        # TODO: Ledger producer background task here.

    def __str__(self) -> str:
        return str(self.user_id)
