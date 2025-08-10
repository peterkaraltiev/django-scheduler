from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser
from schedules.models import Schedule


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'

class ProfileDetailsView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = CustomUser
    template_name = 'accounts/profile_view.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(id=self.kwargs['pk'])
        schedules_list = Schedule.objects.filter(user=user).order_by('-date')

        paginator = Paginator(schedules_list, 8)
        page_number = self.request.GET.get('page')
        context['schedules'] = paginator.get_page(page_number)
        return context