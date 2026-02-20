# OctoFit Tracker Backend

Django REST API backend for the OctoFit Tracker fitness application.

## Setup

1. Create and activate virtual environment:
```bash
cd octofit-tracker/backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
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

**Endpoint:** `GET /api/health/`

**Description:** Returns the current health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "service": "OctoFit Tracker API",
  "timestamp": "2026-02-20T14:32:27.882550+00:00"
}
```

**Status Code:** 200 OK

**Example:**
```bash
curl http://localhost:8000/api/health/
```

## Configuration

The application is configured to work in both local development and GitHub Codespaces environments. The `ALLOWED_HOSTS` setting automatically includes the Codespaces URL when running in a Codespace.

### Environment Variables

The following environment variables can be used to configure the application:

- **DJANGO_SECRET_KEY**: Secret key for Django (defaults to development key if not set)
- **DJANGO_DEBUG**: Set to 'False' to disable debug mode in production (defaults to 'True')
- **CODESPACE_NAME**: Automatically set by GitHub Codespaces, used to configure ALLOWED_HOSTS and CORS

**Example for production:**
```bash
export DJANGO_SECRET_KEY='your-production-secret-key'
export DJANGO_DEBUG='False'
python manage.py runserver
```

## Technologies

- Django 4.2.26 (patched for security vulnerabilities)
- Django REST Framework 3.14.0
- Django CORS Headers 4.5.0
