from django.urls import path, include
from .views import GetUserAPI

urlpatterns = [
    path('', GetUserAPI.as_view()),            # GET
]