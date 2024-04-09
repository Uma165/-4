from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', )
    search_fields = ('text',)
    list_filter = ('date_created',)
    list_display = ('text',)

