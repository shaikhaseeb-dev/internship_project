from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TelegramUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'telegram_username', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('telegram_username', 'phone_number')}),
    )
    search_fields = ('username', 'email', 'telegram_username')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username', 'telegram_id', 'user', 'created_at')
    search_fields = ('username', 'first_name', 'last_name', 'telegram_id')
    list_filter = ('created_at',)
    raw_id_fields = ('user',)
    readonly_fields = ('created_at',)