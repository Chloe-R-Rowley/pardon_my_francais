from rest_framework import serializers
from .models import Level, Lesson, SubLevel, TestResult

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class SubLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLevel
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'