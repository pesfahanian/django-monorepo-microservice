from django.contrib import admin

from common.admin import TemporalModelAdmin

from apps.ledger.models import Entry


@admin.register(Entry)
class EntryAdmin(TemporalModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'user_id',
        'amount',
        'type',
        'transaction_id',
    ) + TemporalModelAdmin.list_display
