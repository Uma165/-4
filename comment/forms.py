from django import forms

from comment.models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(max_length=128, label='Имя')
    text = forms.CharField(widget=forms.Textarea, label='Комментарий')