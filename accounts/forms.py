from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username', 'email', 'profile_picture')

        help_texts = {
            'username': None,
            'password': None,
            'email': None,
            'profile_picture': None,
            'password1': None,
            'password2': None
        }
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            })
        }

