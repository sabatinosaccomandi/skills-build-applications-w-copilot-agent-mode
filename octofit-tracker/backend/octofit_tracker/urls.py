"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import os

def health_check(request):
    """Health check endpoint that returns the status of the application."""
    return JsonResponse({
        'status': 'healthy',
        'message': 'OctoFit Tracker API is running',
        'version': '1.0.0'
    })

def api_root(request):
    """API root endpoint that lists available endpoints."""
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
    
    return JsonResponse({
        'message': 'Welcome to OctoFit Tracker API',
        'endpoints': {
            'health': f'{base_url}/api/health/',
            'admin': f'{base_url}/admin/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/health/', health_check, name='health-check'),
]
