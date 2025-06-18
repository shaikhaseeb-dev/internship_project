# api/apps.py
from django.apps import AppConfig
import os
import socket

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        # Only start in main Django process (not autoreloader or celery)
        if os.environ.get('RUN_MAIN') and not os.environ.get('CELERY_WORKER_RUNNING'):
            try:
                from .telegram_bot import setup_bot
                setup_bot()
            except Exception as e:
                print(f"Bot setup skipped: {e}")