from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ListFilesView, UploadFileAPI

urlpatterns = [
    path('', ListFilesView.as_view(), name='getFileList'),
    path('upload/', UploadFileAPI.as_view(), name='fileupload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)