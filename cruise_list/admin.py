from django.contrib import admin

from cruise_list.models import Cruise, Room


class RoomInlineAdmin(admin.StackedInline):
    model = Room
    list_display = ['category', 'price', 'count']
    extra = 1


@admin.register(Cruise)
class CruiseAdmin(admin.ModelAdmin):
    readonly_fields = ['publish_date', 'edit_date']
    list_display = ['title', 'publish_date', 'edit_date']
    list_filter = ['publish_date', 'edit_date']
    search_fields = ['title']
    inlines = [RoomInlineAdmin]
