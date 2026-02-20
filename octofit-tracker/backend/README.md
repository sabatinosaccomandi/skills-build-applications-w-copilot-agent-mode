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

## Technology Stack

- Django 4.1.7
- Django REST Framework 3.14.0
- django-cors-headers 4.5.0
- Python 3.x
