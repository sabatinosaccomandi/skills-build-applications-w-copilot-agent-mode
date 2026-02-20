from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint for the OctoFit Tracker API.
    Returns the current status of the API.
    """
    return Response({
        'status': 'healthy',
        'service': 'OctoFit Tracker API',
        'timestamp': timezone.now().isoformat()
    }, status=status.HTTP_200_OK)
