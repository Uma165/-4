from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect, Http404, reverse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login

from django.views import View


from .forms import UserRegisterForm, UserProfileForm, get_preferred_cruise_url_params
from .models import Profile
from .utils import login_required





class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            url = reverse('confirm-registration', kwargs={'token': user.profile.email_token})
            html_message = render_to_string('message/notification_message.html', context={
                    'username': user.username,
                    'url': request.build_absolute_uri(url)
                }
            )
            message = strip_tags(html_message)
            send_mail(subject=f'Подтверждение регистрации {user.username}',
                      message=message,
                      html_message=html_message,
                      from_email='admin@sity.ru',
                      recipient_list=[user.email])

            messages.success(request,
                f'Ваш аккаунт создан. Пройдите по ссылке из письма для подтверждения email!')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form})


class ProfileView(View):
    template = 'users/profile.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        form = UserProfileForm.from_user(user)
        appeals = request.user.appeals.order_by('-date')
        cruise_preferred_url_params = get_preferred_cruise_url_params(request.user)
        return render(request, self.template, {'form': form, 'appeals': appeals,
            'cruise_url_params': cruise_preferred_url_params})

    @method_decorator(login_required)
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save_user(request)
            return redirect('profile')
        appeals = request.user.appeals.order_by('-date')
        return render(request, self.template, {'form': form, 'appeals': appeals})


class ConfirmRegistration(View):
    def get(self, request, token, *args, **kwargs):
        try:
            profile = Profile.confirm_email_by_token(token)
            login(request, profile.user)
        except Profile.DoesNotExist:
            return Http404()
        return redirect('profile')

