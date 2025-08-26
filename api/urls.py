# api/urls.py

from django.urls import path
from .views import public, private, register, health_check
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('public/', public, name='public'),
    path('private/', private, name='private'),
    path('register/', register, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('health/', health_check, name='health_check'), # The required health check
]