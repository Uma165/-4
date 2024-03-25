from django.contrib import admin

from page.models import Page


@admin.register(Page)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']