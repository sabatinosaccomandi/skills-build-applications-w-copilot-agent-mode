#!/bin/bash
# Test script for OctoFit Tracker Health Check API

echo "Testing OctoFit Tracker Health Check API..."
echo "============================================"
echo ""

# Test the health check endpoint
echo "GET /api/health/"
echo "Response:"
curl -s http://localhost:8000/api/health/ | python3 -m json.tool
echo ""

echo "Health check test completed successfully!"
