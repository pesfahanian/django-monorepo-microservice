from django.db import models
from django.utils import timezone


class DefaultManager(models.Manager):
    pass


class ToggleableModelManager(DefaultManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_enabled=True, )
