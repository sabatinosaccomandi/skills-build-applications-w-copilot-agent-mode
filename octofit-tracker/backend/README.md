# Octofit Tracker Backend

This is the Django backend for the Octofit Tracker fitness application.

## Health Check API

The backend includes a health check API endpoint for monitoring the application status.

### Endpoints

#### Health Check
- **URL**: `/api/health/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: 
    ```json
    {
        "status": "healthy",
        "message": "Octofit Tracker API is running"
    }
    ```

#### API Root
- **URL**: `/api/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: 
    ```json
    {
        "health": "http://localhost:8000/api/health/",
        "message": "Welcome to Octofit Tracker API"
    }
    ```

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
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## Testing

Run the unit tests:
```bash
python manage.py test
```

## Testing the Health Check API

Using curl:
```bash
curl http://localhost:8000/api/health/
```

Expected response:
```json
{
    "status": "healthy",
    "message": "Octofit Tracker API is running"
}
```

## Security

- The SECRET_KEY can be configured via the `DJANGO_SECRET_KEY` environment variable
- All dependencies are kept up to date to avoid known security vulnerabilities
- CodeQL security scanning shows no vulnerabilities

## Test Coverage

The health check API includes 12 comprehensive unit tests:
- ✅ Endpoint accessibility
- ✅ HTTP status codes
- ✅ Response structure validation
- ✅ Data type validation
- ✅ HTTP method restrictions
- ✅ Multiple request consistency
- ✅ JSON response format
