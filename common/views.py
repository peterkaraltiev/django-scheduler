from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from schedules.models import Schedule


# Create your views here.

class Dashboard(ListView):
    model = Schedule
    template_name = "common/dashboard.html"
    context_object_name = 'schedules'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')

        if query:
            context['schedules'] = Schedule.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(user__username__icontains=query) | Q(tasks__description__icontains = query))

        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()
        return context