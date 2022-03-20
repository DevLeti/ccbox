from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.serializers import GetUserSerializer, CreateUserSerializer


# Create your views here.

class GetUserAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GetUserSerializer

    def get_queryset(self):
        return User.objects.filter(id=1)

class CreateUserAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer