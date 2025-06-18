from django.urls import path
from .views import register
from .views import (
    test_view,
    public,
    private,
    register
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('test/', test_view, name='test'),
    path('public/', public, name='public'),
    path('private/', private, name='private'),
    path('register/', register, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]