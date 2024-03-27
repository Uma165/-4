from django.contrib import admin

from appeal.models import Appeal

from appeal.models import Answer


@admin.register(Appeal)
class AppealFormAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['contact', 'сapacity']
    readonly_fields = ['date',]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['get_id', 'author', 'send_date', 'update_date']
    list_filter = ['send_date', 'update_date']
    search_fields = ['text']
    readonly_fields = ['send_date', 'update_date']

    def get_id(self, obj):
        return obj.appeal.id
