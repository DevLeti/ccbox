from django.urls import path, include
from .views import GetUserAPI, CreateUserAPI, LoginUserAPI

urlpatterns = [
    path('', GetUserAPI.as_view()),            # GET
    path('signup/', CreateUserAPI.as_view()),
    path('signin/', LoginUserAPI.as_view())
]