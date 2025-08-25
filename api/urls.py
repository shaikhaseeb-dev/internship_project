from django.urls import path
from django.http import JsonResponse
from .views import (
    test_view,
    public,
    private,
    register
)
from rest_framework.authtoken.views import obtain_auth_token

# Health check view
def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('test/', test_view, name='test'),
    path('public/', public, name='public'),
    path('private/', private, name='private'),
    path('register/', register, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # New health endpoint
    path('health/', health, name='health'),
]
