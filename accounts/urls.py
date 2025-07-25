from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views import RegisterView

urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]