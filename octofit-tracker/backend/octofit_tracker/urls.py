"""
URL configuration for octofit_tracker project.
"""
from django.contrib import admin
from django.urls import path
from .views import health_check, api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/health/', health_check, name='health-check'),
]
