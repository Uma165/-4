from django.urls import path

from cruise_list.views import СruiseListView

app_name = "cruise"

urlpatterns = [
    path('', СruiseListView.as_view(), name='cruise_list'),
]