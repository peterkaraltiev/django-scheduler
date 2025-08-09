from django.urls import path

from .views import ScheduleCreateView

urlpatterns = [
    path('create_schedule/', ScheduleCreateView.as_view(), name='create_schedule'),
]