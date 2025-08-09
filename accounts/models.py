from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(default='profile_pictures/pfp_placeholder.jpeg', upload_to='profile_pictures')
