from django.core.management.base import BaseCommand
from api.telegram_bot import run_bot

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        run_bot()