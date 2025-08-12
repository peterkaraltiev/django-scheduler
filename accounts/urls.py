from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts import views
from accounts.views import RegisterView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile_view/<int:pk>', ProfileDetailsView.as_view(), name='profile_view'),
    path('profile_edit/<int:pk>', ProfileEditView.as_view(), name='profile_edit'),
    path('profile_delete/<int:pk>', ProfileDeleteView.as_view(), name='profile_delete'),
]