from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer
from rest_framework import generics, permissions


# Create your views here.


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]