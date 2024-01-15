from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=255)

class Lesson(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    phrases = models.JSONField()
    images = models.JSONField()
    translations = models.JSONField()
    audio = models.FileField(upload_to='audio/', null=True, blank=True)

class SubLevel(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sublevel = models.ForeignKey(SubLevel, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    tokens_received = models.PositiveIntegerField()
    badges_earned = models.JSONField()