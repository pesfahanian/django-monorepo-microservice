from django.contrib import admin


class AbstractToggleableModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_enabled',
    )
    list_filter = ('is_enabled', )
    search_fields = ('name_en', )
