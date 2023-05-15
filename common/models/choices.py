from django.db import models
from django.utils.translation import gettext_lazy as _


class TransactionStatus(models.IntegerChoices):
    PENDING = 0, _('Pending')
    SUCCESS = 1, _('Success')
    FAIL = 2, _('Fail')


class TransactionType(models.IntegerChoices):
    WITHDRAW = 0, _('Withdraw')
    DEPOSIT = 1, _('Deposit')
