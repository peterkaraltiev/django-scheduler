from django.shortcuts import render
from django.views.generic import ListView

from schedules.models import Schedule


# Create your views here.

class Dashboard(ListView):
    model = Schedule
    template_name = "common/dashboard.html"
    context_object_name = 'schedules'
    paginate_by = 8