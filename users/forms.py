from django import forms
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from .utils import random_token_generator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=128, help_text='Имя')
    surname = forms.CharField(help_text='Фамилия')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.profile = Profile(user=user, email_token=random_token_generator(128))
        if commit:
            user.profile.save()
        return user


class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=128, label='Логин')
    email = forms.EmailField(max_length=128, label='email')
    name = forms.CharField(max_length=128, label='Имя', required=False)
    surname = forms.CharField(max_length=128, label='Фамилия', required=False)
    image = forms.ImageField(label='Аватар', required=False)
    preferred_room_category = forms.ChoiceField(label='Предпочитаемая категория каюты',
            choices=Profile.ROOM_CATEGORIES, required=False)
    preferred_room_price_min = forms.IntegerField(label='Предпочитаемая цена от', required=False)
    preferred_room_price_max = forms.IntegerField(label='Предпочитаемая цена до', required=False)

    def save_user(self, request, commit=True):
        user: User = request.user

        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']

        try:
            _ = user.profile.pk
        except User.profile.RelatedObjectDoesNotExist:
            user.profile = Profile()

        user.profile.preferred_room_category = self.cleaned_data['preferred_room_category']
        user.profile.preferred_room_price_min = self.cleaned_data['preferred_room_price_min']
        user.profile.preferred_room_price_max = self.cleaned_data['preferred_room_price_max']

        image = request.FILES['image'] if 'image' in request.FILES else None
        if image:
            user.profile.image = image

        if commit:
            user.profile.save()
            user.save()

        return user

    @classmethod
    def from_user(cls, user: User):
        user_dict = model_to_dict(user)
        user_dict['name'] = user_dict['first_name']
        user_dict['surname'] = user_dict['last_name']

        preferred_cruise_url = None

        try:
            user_dict['image'] = user.profile.image
            user_dict['preferred_room_category'] = user.profile.preferred_room_category
            user_dict['preferred_room_price_min'] = user.profile.preferred_room_price_min
            user_dict['preferred_room_price_max'] = user.profile.preferred_room_price_max

        except User.profile.RelatedObjectDoesNotExist:
            user_dict['image'] = None
            user_dict['preferred_room_category'] = None

        form = cls(user_dict)
        form._preferred_cruise_url = preferred_cruise_url
        return form


def get_preferred_cruise_url_params(user: User):
    args = []
    try:
        for key, value in {
            'price_range_min': user.profile.preferred_room_price_min,
            'price_range_max': user.profile.preferred_room_price_max,
            'room_category': user.profile.preferred_room_category,
        }.items():
            if value:
                args.append(f'{key}={value}')
        return '&'.join(args)
    except User.profile.RelatedObjectDoesNotExist:
        return ''

