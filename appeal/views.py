import hashlib
from datetime import datetime

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from appeal.forms import AppealForm
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.generic import DetailView

from appeal.models import Appeal


def submit_appeal(request):
    if request.method == 'POST':
        form = AppealForm(request.POST, request.FILES)
        if form.is_valid():
            appeal = form.save(commit=False)

            while True:
                uid = appeal.contact + appeal.type + appeal.сapacity + str(datetime.now().timestamp())
                m = hashlib.sha256()
                m.update(bytes(uid, encoding='utf-8'))
                uid = m.hexdigest()

                if  len(Appeal.objects.filter(uid=uid)) == 0:
                    break

            appeal.uid = uid

            appeal.save()

            html_message = render_to_string('message/notification_message.html', context={'type': appeal.type,
                                                                                           'url': request.build_absolute_uri(f'/appeal/view/{uid}')})
            message = strip_tags(html_message)
            send_mail(subject=f'Обращение №{appeal.id}',
                      message=message,
                      html_message=html_message,
                      from_email='admin@sity.ru',
                      recipient_list=[appeal.email])
            return redirect(reverse('appeal:appeals'))
    else:
        form = AppealForm()
    return render(request, 'appeal/appeal.html', {'form': form})


class AppealDetailView(DetailView):
    model = Appeal
    template_name = 'appeal/appeal_detail.html'
    context_object_name = 'appeal'
    slug_field = 'uid'
    slug_url_kwarg = 'uid'