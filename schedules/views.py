from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import Schedule, Comments, Tasks
from .forms import ScheduleForm, TaskFormSet, CommentForm, TaskForm


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
    template_name = 'schedules/schedule_edit.html'  # you'll create this
    context_object_name = 'schedule'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        TaskFormSet = modelformset_factory(Tasks, form=TaskForm, extra=0, can_delete=True)

        if self.request.POST:
            context['formset'] = TaskFormSet(self.request.POST, queryset=self.object.tasks.all())
        else:
            context['formset'] = TaskFormSet(queryset=self.object.tasks.all())

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save()
            tasks = formset.save(commit=False)

            for task in tasks:
                task.schedule = self.object
                task.save()

            for task in formset.deleted_objects:
                task.delete()

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('schedule_detail', kwargs={'pk': self.object.pk})

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedules/schedule_delete.html'
    success_url = reverse_lazy('home')


class CommentEditView(UpdateView):
    model = Comments
    form_class = CommentForm
    template_name = 'schedules/comment_edit.html'

    def get_success_url(self):
        return reverse_lazy('schedule_detail', kwargs={'pk': self.object.schedule.pk})

class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'schedules/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('schedule_detail', kwargs={'pk': self.object.schedule.pk})