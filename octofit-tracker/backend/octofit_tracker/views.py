"""
Views for the octofit_tracker project.
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def health_check(request):
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        JsonResponse: A JSON response with status and message.
    """
    return JsonResponse({
        'status': 'healthy',
        'message': 'OctoFit Tracker API is running'
    })
