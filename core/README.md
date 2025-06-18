# Django Internship Project

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment
3. Install requirements: `pip install -r requirements.txt`
4. Create `.env` file with required variables
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`

## Environment Variables

- DEBUG
- SECRET_KEY
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- TELEGRAM_BOT_TOKEN

## How to Run Locally

1. Start Django server: `python manage.py runserver`
2. Start Celery worker: `celery -A internship_project worker -l info`
3. Start Telegram bot: `python manage.py telegram_bot`

## API Documentation

### Public Endpoints
- GET /api/public/ - List all public data

### Protected Endpoints
- GET /api/private/ - List user's private data
- POST /api/private/ - Create new private data

### Authentication
- POST /api/token/ - Obtain JWT token (username, password)
- POST /api/token/refresh/ - Refresh JWT token