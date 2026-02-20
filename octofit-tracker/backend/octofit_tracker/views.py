from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint to verify the API is running.
    Returns the current status and timestamp.
    """
    return Response({
        'status': 'healthy',
        'message': 'OctoFit Tracker API is running',
        'timestamp': timezone.now().isoformat()
    }, status=status.HTTP_200_OK)
