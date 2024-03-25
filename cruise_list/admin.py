from django.contrib import admin

from cruise_list.models import Сruise


@admin.register(Сruise)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ['publish_date', 'edit_date']
    list_display = ['title', 'publish_date', 'edit_date']
    list_filter = ['publish_date', 'edit_date']
    search_fields = ['title']