from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint to verify the API is running.
    Returns the current status and timestamp.
    """
    return Response({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'OctoFit Tracker API'
    }, status=status.HTTP_200_OK)
