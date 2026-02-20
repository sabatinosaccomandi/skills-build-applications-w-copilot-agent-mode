"""
URL configuration for octofit_tracker project.
"""
import os
from django.contrib import admin
from django.urls import path
from .views import health_check, api_root

# Get codespace URL if running in GitHub Codespaces
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/health/', health_check, name='health-check'),
]
