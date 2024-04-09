from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.views.generic import DetailView, View

from appeal.forms import AppealForm
from appeal.models import Appeal
from cruise_list.models import Cruise


class SubmitAppealView(View):
    def get(self, request):
        contact = email = ''
        if request.user.is_authenticated:
            email = request.user.email
            contact = request.user.get_full_name()
        cruise_id = request.GET.get('cruise')
        cruise = Cruise.objects.get(pk=cruise_id) if cruise_id else None
        form = AppealForm(initial={'email': email, 'contact': contact, 'cruise': cruise})
        return render(request, 'appeal/appeal.html', {'form': form})

    def post(self, request):
        form = AppealForm(request.POST, request.FILES)

        if form.is_valid():
            appeal = form.save(commit=True)
            if request.user.is_authenticated:
                appeal.user = request.user
            appeal.save()

            html_message = render_to_string('message/notification_message.html', context={
                    'cruise_title': appeal.cruise.title,
                    'url': request.build_absolute_uri(f'/appeal/view/{appeal.uid}')
                }
            )
            message = strip_tags(html_message)
            send_mail(subject=f'Обращение №{appeal.id}',
                      message=message,
                      html_message=html_message,
                      from_email='admin@sity.ru',
                      recipient_list=[appeal.email])
            return redirect('appeal:view', uid=appeal.uid)

        return render(request, 'appeal/appeal.html', {'form': form})



class AppealDetailView(DetailView):
    model = Appeal
    template_name = 'appeal/appeal_detail.html'
    context_object_name = 'appeal'
    slug_field = 'uid'
    slug_url_kwarg = 'uid'
