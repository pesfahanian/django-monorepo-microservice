from django.contrib import admin
from django.db import models


class ToggleableModelAdmin(admin.ModelAdmin):
    list_display = ('is_enabled', )


class TemporalModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        '_created_at',
        '_updated_at',
    )
    list_display = (
        '_created_at',
        '_updated_at',
    )
    ordering = ('-created_at', )

    def _created_at(self, obj: models.Model) -> str:
        return obj.created_at.strftime("%d %b %Y %H:%M:%S")

    def _updated_at(self, obj: models.Model) -> str:
        return obj.updated_at.strftime("%d %b %Y %H:%M:%S")
