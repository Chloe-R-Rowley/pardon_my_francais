# lessons/urls.py

from django.urls import path
from .views import get_lessons

urlpatterns = [
    path('lessons/', get_lessons, name='get_lessons'),
]
