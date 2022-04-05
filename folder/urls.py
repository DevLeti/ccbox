from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ListFoldersAPI, NewFolderAPI

urlpatterns = [
    path('', ListFoldersAPI.as_view(), name='getFolderList'),
    path('new/', NewFolderAPI.as_view(), name='NewFolder')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)