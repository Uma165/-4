from django.urls import path

from appeal import views

app_name = 'appeal'

urlpatterns = [
    path('submit', views.SubmitAppealView.as_view(), name='submit'),
    path('view/<slug:uid>', views.AppealDetailView.as_view(), name='view')
]
