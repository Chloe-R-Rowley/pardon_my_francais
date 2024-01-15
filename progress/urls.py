# progress/urls.py

from django.urls import path
from .views import get_progress

urlpatterns = [
    path('progress/', get_progress, name='get_progress'),
]
