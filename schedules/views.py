from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .models import Schedule
from .forms import ScheduleForm, TaskFormSet

class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedules/create_schedule.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        formset = TaskFormSet(prefix='form')
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        formset = TaskFormSet(request.POST, prefix='form')

        if form.is_valid() and formset.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            tasks = formset.save(commit=False)
            for task in tasks:
                task.schedule = schedule
                task.save()
            return redirect('home')  # or wherever you want
        return render(request, self.template_name, {'form': form, 'formset': formset})