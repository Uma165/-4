from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('confirm-registration/<str:token>/', views.ConfirmRegistration.as_view(),
         name='confirm-registration'),
]
