from django.urls import path

from .views import ScheduleCreateView, ScheduleDetailView

urlpatterns = [
    path('create_schedule/', ScheduleCreateView.as_view(), name='create_schedule'),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
]