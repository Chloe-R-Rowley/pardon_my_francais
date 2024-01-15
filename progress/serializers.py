from rest_framework import serializers
from django.contrib.auth.models import User
from levels.serializers import LevelSerializer, LessonSerializer, SubLevelSerializer, TestResultSerializer
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    levels_completed = LevelSerializer(many=True)
    lessons_completed = LessonSerializer(many=True)
    sublevels_completed = SubLevelSerializer(many=True)
    test_results = TestResultSerializer(many=True)

    class Meta:
        model = Progress
        fields = '__all__'