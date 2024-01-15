# progress/models.py

from django.db import models
from django.contrib.auth.models import User
from levels.models import Level, Lesson, SubLevel, TestResult

class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    levels_completed = models.ManyToManyField(Level, blank=True, related_name='progress_levels_completed')
    lessons_completed = models.ManyToManyField(Lesson, blank=True, related_name='progress_lessons_completed')
    sublevels_completed = models.ManyToManyField(SubLevel, blank=True, related_name='progress_sublevels_completed')
    test_results = models.ManyToManyField(TestResult, blank=True, related_name='progress_test_results')
    current_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='progress_current_level')
    current_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, related_name='progress_current_lesson')
    total_tests_taken = models.PositiveIntegerField(default=0)
    total_tokens_received = models.PositiveIntegerField(default=0)
