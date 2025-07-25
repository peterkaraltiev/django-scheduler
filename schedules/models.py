from django.db import models

# Create your models here.

class Schedule(models.Model):
    created = models.DateTimeField(auto_now_add=True)
