from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.managers import DefaultManager, ToggleableModelManager


class UUIDModel(models.Model):

    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    def __str__(self) -> str:
        return str(self.id)


class ToggleableModel(models.Model):

    class Meta:
        abstract = True

    is_enabled = models.BooleanField(
        _('Is Enabled'),
        default=True,
    )

    objects = DefaultManager()
    enabled_objects = ToggleableModelManager()

    def enable(self) -> None:
        self.is_enabled = True
        self.save()

    def disable(self) -> None:
        self.is_enabled = False
        self.save()


class TemporalModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True,
    )
