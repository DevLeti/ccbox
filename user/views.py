from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.serializers import GetUserSerializer, CreateUserSerializer, MyTokenObtainPairSerializer


class LoginUserAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data

        if request.data['username'] == 'None':
            return Response({'message': 'login failed'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(
            {
                'username': request.data['username'],
                'token': token['access']
            }
        )

class GetUserAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GetUserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class CreateUserAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer