from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthCheckTestCase(APITestCase):
    """Test cases for the health check API endpoint"""
    
    def test_health_check_endpoint(self):
        """Test that the health check endpoint returns 200 OK"""
        url = reverse('health-check')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'healthy')
        self.assertEqual(response.data['service'], 'OctoFit Tracker API')
        self.assertIn('timestamp', response.data)
    
    def test_health_check_method_not_allowed(self):
        """Test that POST requests are not allowed on health check endpoint"""
        url = reverse('health-check')
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
