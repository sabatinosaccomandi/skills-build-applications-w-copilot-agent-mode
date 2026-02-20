# OctoFit Tracker Backend

Django REST API backend for the OctoFit Tracker fitness application.

## Features

- Health check API endpoint
- Django REST Framework
- CORS support for frontend integration
- Codespaces-ready configuration

## Setup

### Prerequisites

- Python 3.8+
- Virtual environment

### Installation

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## API Endpoints

### Health Check

**GET** `/api/health/`

Returns the current status of the API.

**Response:**
```json
{
    "status": "healthy",
    "message": "OctoFit Tracker API is running",
    "timestamp": "2026-02-20T14:41:20.958389+00:00"
}
```

## Testing

Run the test script to verify the health check endpoint:

```bash
./test_health_check.sh
```

Or use curl directly:

```bash
curl http://localhost:8000/api/health/
```

## Development

The application is configured to work in GitHub Codespaces. The `ALLOWED_HOSTS` setting automatically includes the Codespace URL when the `CODESPACE_NAME` environment variable is set.

## Technologies

- Django 4.2.28 (security patched)
- Django REST Framework 3.14.0
- django-cors-headers 4.5.0
- Python 3.12+

**Security**: All dependencies have been updated to patched versions to address known vulnerabilities.
