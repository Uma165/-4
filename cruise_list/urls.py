from django.urls import path

from cruise_list.views import СruiseListView
from cruise_list.views import cruise_detail_view

app_name = "cruise"

urlpatterns = [
    path('', СruiseListView.as_view(), name='cruise_list'),
    path('cruise/<int:pk>/', cruise_detail_view, name='too'),

]