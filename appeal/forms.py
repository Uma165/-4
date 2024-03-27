from django import forms

from appeal.models import Appeal


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        exclude = ['id', 'uid', 'status']