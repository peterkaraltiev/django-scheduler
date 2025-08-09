from django import forms
from .models import Schedule, Tasks
from django.forms.models import inlineformset_factory

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'date', 'picture']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Schedule description...'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['description', 'time']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task description...'
            }),
        }

TaskFormSet = inlineformset_factory(Schedule, Tasks, form=TaskForm, extra=1, can_delete=False)