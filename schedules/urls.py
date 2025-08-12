from django.urls import path

from .views import ScheduleCreateView, ScheduleDetailView, ScheduleEditView, ScheduleDeleteView, CommentEditView, \
    CommentDeleteView

urlpatterns = [
    path('create_schedule/', ScheduleCreateView.as_view(), name='create_schedule'),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedule_edit/<int:pk>/', ScheduleEditView.as_view(), name='schedule_edit'),
    path('schedule_delete/<int:pk>/', ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('comment_edit/<int:pk>/', CommentEditView.as_view(), name='comment_edit'),
    path('comment_delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]