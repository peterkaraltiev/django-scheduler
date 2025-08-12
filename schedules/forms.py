from django import forms
from .models import Schedule, Tasks, Comments
from django.forms.models import inlineformset_factory

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'date', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Schedule description...'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            })
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['schedule']
        fields = ['description', 'time']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task description...'
            }),
        }

TaskFormSet = inlineformset_factory(Schedule, Tasks, form=TaskForm, extra=1, can_delete=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }