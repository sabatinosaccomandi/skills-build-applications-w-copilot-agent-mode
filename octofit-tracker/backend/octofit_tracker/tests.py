"""
Unit tests for the Octofit Tracker API health check endpoint.
"""
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json


class HealthCheckAPITestCase(TestCase):
    """Test cases for the health check API endpoint."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.health_check_url = reverse('health-check')
    
    def test_health_check_endpoint_exists(self):
        """Test that the health check endpoint exists and is accessible."""
        response = self.client.get(self.health_check_url)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_health_check_returns_200(self):
        """Test that the health check endpoint returns HTTP 200 OK."""
        response = self.client.get(self.health_check_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_health_check_returns_json(self):
        """Test that the health check endpoint returns JSON data."""
        response = self.client.get(self.health_check_url)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_health_check_response_structure(self):
        """Test that the health check response has the correct structure."""
        response = self.client.get(self.health_check_url)
        data = response.json()
        
        # Check that response contains required fields
        self.assertIn('status', data)
        self.assertIn('message', data)
    
    def test_health_check_status_value(self):
        """Test that the health check status field has the correct value."""
        response = self.client.get(self.health_check_url)
        data = response.json()
        
        self.assertEqual(data['status'], 'healthy')
    
    def test_health_check_message_value(self):
        """Test that the health check message field has the correct value."""
        response = self.client.get(self.health_check_url)
        data = response.json()
        
        self.assertEqual(data['message'], 'Octofit Tracker API is running')
    
    def test_health_check_only_accepts_get(self):
        """Test that the health check endpoint only accepts GET requests."""
        # POST should not be allowed
        response = self.client.post(self.health_check_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
        # PUT should not be allowed
        response = self.client.put(self.health_check_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
        # DELETE should not be allowed
        response = self.client.delete(self.health_check_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_health_check_response_data_types(self):
        """Test that the health check response fields have correct data types."""
        response = self.client.get(self.health_check_url)
        data = response.json()
        
        # Both fields should be strings
        self.assertIsInstance(data['status'], str)
        self.assertIsInstance(data['message'], str)
    
    def test_health_check_multiple_requests(self):
        """Test that the health check endpoint consistently returns the same response."""
        response1 = self.client.get(self.health_check_url)
        response2 = self.client.get(self.health_check_url)
        response3 = self.client.get(self.health_check_url)
        
        # All responses should be identical
        self.assertEqual(response1.json(), response2.json())
        self.assertEqual(response2.json(), response3.json())
        
        # All should return 200 OK
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)


class APIRootTestCase(TestCase):
    """Test cases for the API root endpoint."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.api_root_url = reverse('api-root')
    
    def test_api_root_endpoint_exists(self):
        """Test that the API root endpoint exists and is accessible."""
        response = self.client.get(self.api_root_url)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_root_returns_200(self):
        """Test that the API root endpoint returns HTTP 200 OK."""
        response = self.client.get(self.api_root_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_root_includes_health_endpoint(self):
        """Test that the API root response includes the health check endpoint."""
        response = self.client.get(self.api_root_url)
        data = response.json()
        
        self.assertIn('health', data)
        self.assertIn('/api/health/', data['health'])
