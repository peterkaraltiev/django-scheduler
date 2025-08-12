from django.contrib import admin

from schedules.models import Schedule, Tasks, Comments


# Register your models here.

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'user')

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('time', 'description', 'schedule')

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user')