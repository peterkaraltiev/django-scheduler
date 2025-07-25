from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='static/pfp_placeholder.jpeg', upload_to='profile_pictures')