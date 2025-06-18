import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from django.conf import settings
from .models import TelegramUser
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        TelegramUser.objects.get_or_create(
            telegram_id=user.id,
            defaults={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name or ''
            }
        )
        await update.message.reply_text(f"Hello {user.first_name}! You are registered.")
    except Exception as e:
        logger.error(f"Error in start handler: {e}")

def run_bot():
    try:
        token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
        if not token:
            raise ValueError("TELEGRAM_BOT_TOKEN not set in settings")
            
        app = Application.builder().token(token).build()
        app.add_handler(CommandHandler("start", start))
        logger.info("Bot starting...")
        app.run_polling()
    except Exception as e:
        logger.error(f"Bot failed: {e}")