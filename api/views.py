from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .tasks import send_welcome_email
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from telegram import Bot
from django.conf import settings
from django.http import JsonResponse

User = get_user_model()



@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    """Public endpoint accessible to anyone"""
    return Response({"message": "This is a public endpoint"})

def health_check(request):
    """
    A simple health check endpoint.
    """
    data = {
        'status': 'ok',
        'message': 'Service is healthy'
    }
    return JsonResponse(data)

@api_view(['GET'])
def private(request):
    """Private endpoint requiring authentication"""
    return Response({"message": f"Hello {request.user.username}! This is a private endpoint"})


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """User registration endpoint"""
    try:
        data = request.data
        required_fields = ['username', 'email', 'password']
        if not all(field in data for field in required_fields):
            return Response({"error": "Missing required fields"}, status=400)

        if User.objects.filter(username=data['username']).exists():
            return Response({"error": "Username already exists"}, status=400)

        if User.objects.filter(email=data['email']).exists():
            return Response({"error": "Email already exists"}, status=400)

        # Create user ONLY ONCE
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        # Create token for the new user
        token = Token.objects.create(user=user)

        # Send the welcome email task
        send_welcome_email.delay(user.email)

        return Response({
            "message": "User created successfully",
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        }, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=500)