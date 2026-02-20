# OctoFit Tracker Backend

This is the backend API for the OctoFit Tracker fitness application.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. (Optional) Set environment variables for development:
```bash
export DJANGO_DEBUG=True
export DJANGO_SECRET_KEY="your-secret-key-here"
```

Note: For production, always set `DJANGO_DEBUG=False` and use a secure secret key.

## Health Check API

The health check API endpoint is available at `/api/health/` and returns a simple status to verify the API is running.

### Endpoint

- **URL**: `/api/health/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**: 
    ```json
    {
      "status": "healthy",
      "message": "OctoFit Tracker API is running"
    }
    ```

### Testing the Health Check

You can test the health check endpoint using curl:

```bash
curl http://localhost:8000/api/health/
```

## Running Tests

To run all unit tests:

```bash
python manage.py test
```

To run only the health check tests:

```bash
python manage.py test octofit_tracker.tests.HealthCheckAPITestCase
```

### Test Coverage

The health check API has comprehensive unit tests covering:

1. **HTTP Status Code**: Verifies the endpoint returns 200 OK
2. **Content Type**: Ensures response is JSON
3. **Response Structure**: Validates the presence of 'status' and 'message' fields
4. **Response Values**: Checks correct values for status and message
5. **HTTP Methods**: Ensures only GET requests are allowed (POST, PUT, DELETE return 405)
6. **Data Types**: Validates that response fields are strings

## Running the Development Server

```bash
# Set DEBUG to True for development
export DJANGO_DEBUG=True
python manage.py runserver 8000
```

The API will be available at `http://localhost:8000/`
