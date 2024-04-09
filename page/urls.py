from django.urls import path

from page.views import PageListView

app_name = "page"

urlpatterns = [
    path('', PageListView.as_view(), name="main")
]
