# progress/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Progress
from .serializers import ProgressSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_progress(request):
    user = request.user
    progress, created = Progress.objects.get_or_create(user=user)
    serializer = ProgressSerializer(progress)
    return Response(serializer.data)
