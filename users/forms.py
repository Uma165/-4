from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=128, help_text='Имя')
    surname = forms.CharField(help_text='Фамилия')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']