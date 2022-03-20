from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer
# Create your views here.

class GetUserAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=1)
