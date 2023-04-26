from django.contrib import admin

from apps.wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        '_created_at',
        '_updated_at',
    )
    list_display = (
        'user_id',
        'balance',
        '_created_at',
        '_updated_at',
        'is_enabled',
    )
    ordering = ('-created_at', )

    def _created_at(self, obj: Wallet):
        ann = obj.created_at.strftime("%d %b %Y %H:%M:%S")
        print(f'{type(ann) = }')
        return ann

    def _updated_at(self, obj: Wallet):
        return obj.updated_at.strftime("%d %b %Y %H:%M:%S")
