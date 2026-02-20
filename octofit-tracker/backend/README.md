# OctoFit Tracker Backend

This is the Django backend for the OctoFit Tracker application, a fitness tracking app.

## Features

- Health Check API endpoint
- Django REST Framework integration
- CORS support for frontend integration
- Codespace environment support

## Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check

**Endpoint:** `/api/health/`  
**Method:** `GET`  
**Description:** Returns the current health status of the API

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-20T14:32:09.765851",
  "service": "OctoFit Tracker API"
}
```

## Testing

Run tests with:
```bash
python manage.py test
```

## Environment Support

The backend supports both local development and GitHub Codespaces:

- **Local:** API runs on `http://localhost:8000`
- **Codespaces:** Automatically configures for `https://{CODESPACE_NAME}-8000.app.github.dev`

### Environment Variables

The following environment variables can be configured:

- `DJANGO_SECRET_KEY`: Secret key for Django (defaults to development key if not set)
- `DJANGO_DEBUG`: Set to 'False' to disable debug mode in production (defaults to 'True')
- `CODESPACE_NAME`: Automatically set by GitHub Codespaces for hostname configuration

**Production Configuration Example:**
```bash
export DJANGO_SECRET_KEY='your-production-secret-key-here'
export DJANGO_DEBUG='False'
python manage.py runserver
```

## Technology Stack

- Django 4.2.28 (security patched)
- Django REST Framework 3.14.0
- django-cors-headers 4.5.0
- Python 3.x

All dependencies are kept up-to-date with security patches to ensure the application is protected against known vulnerabilities.
