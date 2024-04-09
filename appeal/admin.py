from django.contrib import admin

from appeal.models import Appeal, Answer


class AnswerAdminInline(admin.StackedInline):
    model = Answer
    extra = 0
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'
    readonly_fields = ['author', 'id']


@admin.register(Appeal)
class AppealFormAdmin(admin.ModelAdmin):
    # date_hierarchy = 'date'
    exclude = []
    list_display = ['date', 'contact', 'capacity', 'status']
    readonly_fields = ['uid', 'date']
    inlines = [AnswerAdminInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    date_hierarchy = 'send_date'
    exclude = []
    list_display = ['get_id', 'author', 'send_date', 'update_date']
    list_filter = ['send_date', 'update_date']
    search_fields = ['text']
    readonly_fields = ['send_date', 'update_date']

    def get_id(self, obj):
        return obj.appeal.id

    def save_model(self, request, obj, form, change):
        """Assign current user on save"""
        obj.author = request.user
        super().save_model(request, obj, form, change)
