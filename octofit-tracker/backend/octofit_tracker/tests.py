"""
Unit tests for the health check API endpoint.
"""
from django.test import TestCase, Client
from django.urls import reverse
import json


class HealthCheckAPITestCase(TestCase):
    """Test cases for the health check API endpoint."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.health_check_url = reverse('health-check')
    
    def test_health_check_returns_200_status_code(self):
        """Test that health check endpoint returns 200 OK status."""
        response = self.client.get(self.health_check_url)
        self.assertEqual(response.status_code, 200)
    
    def test_health_check_returns_json_response(self):
        """Test that health check endpoint returns JSON response."""
        response = self.client.get(self.health_check_url)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_health_check_response_contains_status(self):
        """Test that health check response contains 'status' field."""
        response = self.client.get(self.health_check_url)
        data = json.loads(response.content)
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_health_check_response_contains_message(self):
        """Test that health check response contains 'message' field."""
        response = self.client.get(self.health_check_url)
        data = json.loads(response.content)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'OctoFit Tracker API is running')
    
    def test_health_check_only_accepts_get_method(self):
        """Test that health check endpoint only accepts GET requests."""
        # Test POST method - should return 405 Method Not Allowed
        response = self.client.post(self.health_check_url)
        self.assertEqual(response.status_code, 405)
        
        # Test PUT method - should return 405 Method Not Allowed
        response = self.client.put(self.health_check_url)
        self.assertEqual(response.status_code, 405)
        
        # Test DELETE method - should return 405 Method Not Allowed
        response = self.client.delete(self.health_check_url)
        self.assertEqual(response.status_code, 405)
    
    def test_health_check_response_structure(self):
        """Test that health check response has the correct structure."""
        response = self.client.get(self.health_check_url)
        data = json.loads(response.content)
        
        # Check that response has exactly 2 keys
        self.assertEqual(len(data), 2)
        
        # Check that both required keys are present
        self.assertIn('status', data)
        self.assertIn('message', data)
        
        # Check that values are strings
        self.assertIsInstance(data['status'], str)
        self.assertIsInstance(data['message'], str)
