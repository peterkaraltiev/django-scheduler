import datetime

from django.db import models

from accounts.models import CustomUser


# Create your models here.

class Schedule(models.Model):
    user = models.ForeignKey(CustomUser, default=1, related_name='schedules', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default="My Schedule")
    picture = models.ImageField(default='schedules_pictures/placeholder_schedule.jpeg', upload_to='schedules_pictures')
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.date.today)

class Tasks(models.Model):
    schedule = models.ForeignKey(Schedule, default=1, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    time = models.TimeField(default=datetime.time)

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, default=1, related_name='comments', on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, default=1, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)