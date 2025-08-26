# core/settings.py
"""
Django settings for core project.
"""

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# --- Basic Setup ---
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Correct ALLOWED_HOSTS - only define it once
ALLOWED_HOSTS = ['internship-project-x0ev.onrender.com', 'localhost', '127.0.0.1']

# --- Application Definitions ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'api.apps.ApiConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Database Configuration ---
DATABASES = {
    'default': dj_database_url.config(
        # Fallback to sqlite for local development
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# --- Password and Internationalization ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static Files Configuration ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Custom App and Framework Settings ---
AUTH_USER_MODEL = 'api.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# --- Celery and Redis Configuration ---
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
CELERY_BROKER_URL = f'{REDIS_URL}/0'
CELERY_RESULT_BACKEND = f'{REDIS_URL}/1'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# --- External Service Configuration ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')