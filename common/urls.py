from django.urls import path

from common import views
from common.views import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='home'),
]