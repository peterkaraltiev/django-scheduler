from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'

class ProfileDisplay(DetailView):
    model = get_user_model()
    template_name = 'accounts/profile_view.html'
    form_class = CustomUserCreationForm

    # def get_context_data(self, **kwargs):
    #     kwargs.update({
    #         "user": CustomUser.objects.get(id=self.request.user.id),
    #     })
    #     return super().get_context_data(**kwargs)