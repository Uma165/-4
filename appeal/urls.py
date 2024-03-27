from django.urls import path

from appeal.views import submit_appeal

from appeal.views import AppealDetailView

app_name = 'appeal'

urlpatterns = [
    path('', submit_appeal, name='appeals'),
    path('view/<slug:uid>', AppealDetailView.as_view(), name='view')
]