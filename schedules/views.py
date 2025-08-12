from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import Schedule, Comments
from .forms import ScheduleForm, TaskFormSet, CommentForm


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


class ScheduleDetailView(LoginRequiredMixin, DetailView):
    model = Schedule
    template_name = 'schedules/schedule_details.html'
    context_object_name = 'schedule'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.schedule = self.object
            comment.save()
            return redirect('schedule_detail', pk=self.object.pk)
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)


class ScheduleEditView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedules/schedule_edit.html'
    success_url = reverse_lazy('home')

    # def get_context_data(self, **kwargs):
    #     schedule = get_object_or_404(Schedule, pk=self.object.pk)
    #     form = ScheduleForm(self.request.POST or None, self.request.FILES or None, instance=schedule)
    #     formset = TaskFormSet(self.request.POST or None, instance=schedule)

class ScheduleDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('home')
    template_name = 'schedules/schedule_delete.html'


class CommentEditView(UpdateView):
    model = Comments
    form_class = CommentForm
    template_name = 'schedules/comment_edit.html'
    success_url = reverse_lazy('home')

class CommentDeleteView(DeleteView):
    model = Comments
    success_url = reverse_lazy('home')
    template_name = 'schedules/comment_delete.html'