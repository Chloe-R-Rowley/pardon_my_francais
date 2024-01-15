# lessons/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Level, Lesson, SubLevel, TestResult
from .serializers import LevelSerializer, LessonSerializer, SubLevelSerializer, TestResultSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_levels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lessons(request, level_id):
    lessons = Lesson.objects.filter(level_id=level_id)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sublevels(request, lesson_id):
    sublevels = SubLevel.objects.filter(lesson_id=lesson_id)
    serializer = SubLevelSerializer(sublevels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_test_result(request):
    user = request.user
    data = request.data
    serializer = TestResultSerializer(data=data)

    if serializer.is_valid():
        test_result = serializer.save(user=user)
        user_profile = user.userprofile
        user_profile.total_tests_taken += 1
        user_profile.total_tokens_received += test_result.tokens_received
        user_profile.save()

        return Response(TestResultSerializer(test_result).data, status=201)

    return Response(serializer.errors, status=400)
