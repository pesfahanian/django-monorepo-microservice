import logging

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import UUIDModel

logger = logging.getLogger('django')


class EntryType(models.IntegerChoices):
    DEBIT = 0, _('Debit')
    CREDIT = 1, _('Credit')


class Entry(UUIDModel):
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    transaction_id = models.UUIDField(_('Transaction ID'), )
    user_id = models.UUIDField(_('User ID'), )

    amount = models.DecimalField(
        default=0,
        max_digits=settings.DECIMAL_MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        validators=[
            MinValueValidator(0),
        ],
    )

    type = models.PositiveSmallIntegerField(
        _('Type'),
        choices=EntryType.choices,
    )

    created_at = models.DateTimeField(_('Created at'), )
    updated_at = models.DateTimeField(_('Updated at'), )
