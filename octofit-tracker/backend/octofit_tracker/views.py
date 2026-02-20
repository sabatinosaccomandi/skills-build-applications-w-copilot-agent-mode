"""
Views for the Octofit Tracker API
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        Response: JSON response with status and message
    """
    return Response({
        'status': 'healthy',
        'message': 'Octofit Tracker API is running'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_root(request):
    """
    API root endpoint that lists available endpoints.
    
    Returns:
        Response: JSON response with available endpoints
    """
    return Response({
        'health': request.build_absolute_uri('/api/health/'),
        'message': 'Welcome to Octofit Tracker API'
    })
