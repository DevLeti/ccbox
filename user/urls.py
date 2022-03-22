from django.urls import path, include
from .views import GetUserInfoAPI, CreateUserAPI, LoginUserAPI

urlpatterns = [
    path('', GetUserInfoAPI.as_view()),            # GET
    path('signup/', CreateUserAPI.as_view()),
    path('signin/', LoginUserAPI.as_view()),
]