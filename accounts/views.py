from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'