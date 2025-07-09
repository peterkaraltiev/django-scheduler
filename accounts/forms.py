from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'profile_picture')

        help_texts = {
            'username': '',
            'password': '',
            'email': '',
            'profile_picture': '',
        }