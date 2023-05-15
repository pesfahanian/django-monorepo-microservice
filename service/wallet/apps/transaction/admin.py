from django.contrib import admin

from common.admin import TemporalModelAdmin, ToggleableModelAdmin

from apps.transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(TemporalModelAdmin, ToggleableModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'id',
        'wallet',
        'amount',
        'type',
        'status',
    ) + TemporalModelAdmin.list_display
