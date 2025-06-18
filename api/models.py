from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    """
    telegram_username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("User's Telegram username")
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=_("User's phone number")
    )

    class Meta:
        verbose_name = _('Custom User')
        verbose_name_plural = _('Custom Users')

    def __str__(self):
        return self.username


class TelegramUser(models.Model):
    """
    Model to store Telegram user information
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='telegram',
        blank=True,
        null=True
    )
    telegram_id = models.BigIntegerField(
        unique=True,
        help_text=_("User's Telegram ID")
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Telegram username")
    )
    first_name = models.CharField(
        max_length=255,
        default='Unknown',  # Default for new records
        blank=True,        # Allow blank in forms
        help_text=_("User's first name from Telegram")
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("User's last name from Telegram")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("When the user was first registered")
    )

    class Meta:
        verbose_name = _('Telegram User')
        verbose_name_plural = _('Telegram Users')

    def __str__(self):
        return f"{self.first_name} (@{self.username})" if self.username else self.first_name