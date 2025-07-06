# ALX Travel App

A comprehensive travel listing platform built with Django REST Framework.

## Features

- **Travel Listings Management**: Create, read, update, and delete travel listings
- **User Authentication**: Secure user registration and authentication
- **API Documentation**: Comprehensive API documentation using Swagger
- **Search & Filter**: Advanced search and filtering capabilities
- **MySQL Database**: Robust database management with MySQL
- **Celery Integration**: Background task processing with Celery and Redis
- **CORS Support**: Cross-Origin Resource Sharing for frontend integration

## Tech Stack

- **Backend**: Django 4.2.7, Django REST Framework
- **Database**: MySQL
- **Task Queue**: Celery with Redis
- **API Documentation**: drf-yasg (Swagger)
- **Environment Management**: django-environ

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx_travel_app.git
   cd alx_travel_app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r alx_travel_app/requirement.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and other settings
   ```

5. Set up MySQL database:
   ```bash
   mysql -u root -p
   CREATE DATABASE alx_travel_app;
   ```

6. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## API Endpoints

### Listings
- `GET /api/v1/listings/` - List all listings
- `POST /api/v1/listings/` - Create a new listing (authenticated)
- `GET /api/v1/listings/{id}/` - Get a specific listing
- `PUT /api/v1/listings/{id}/` - Update a listing (authenticated)
- `DELETE /api/v1/listings/{id}/` - Delete a listing (authenticated)
- `POST /api/v1/listings/{id}/mark_available/` - Mark listing as available
- `POST /api/v1/listings/{id}/mark_unavailable/` - Mark listing as unavailable

### Amenities
- `GET /api/v1/amenities/` - List all amenities
- `GET /api/v1/amenities/{id}/` - Get a specific amenity

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306

# CORS Settings
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Celery Settings
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

## Running with Celery

To run background tasks with Celery:

1. Start Redis server:
   ```bash
   redis-server
   ```

2. Start Celery worker:
   ```bash
   celery -A alx_travel_app worker --loglevel=info
   ```

3. Start Celery beat (for periodic tasks):
   ```bash
   celery -A alx_travel_app beat --loglevel=info
   ```

## Testing

Run the test suite:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License.
