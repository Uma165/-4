from django.urls import path
from . import views


app_name = "cruise"
urlpatterns = [
    path('', views.CruiseListView.as_view(), name='cruise-list'),
    path('<int:pk>/', views.cruise_detail_view, name='cruise-detail'),
    path('<int:pk>/add-comment/', views.AddCommentView.as_view(),
         name='cruise-add-comment')
]
