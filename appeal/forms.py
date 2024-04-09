from django import forms

from appeal.models import Appeal
from cruise_list.models import Cruise


class AppealForm(forms.ModelForm):
    cruise = forms.ModelChoiceField(queryset=Cruise.objects.filter(is_active=True).order_by('-edit_date'))

    class Meta:
        model = Appeal
        exclude = ['id', 'uid', 'status', 'user']
