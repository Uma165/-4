from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_create', )
    search_fields = ('text',)
    list_filter = ('date_of_create',)
    list_display = ('text',)

