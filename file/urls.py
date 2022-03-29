from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import ListFilesView, UploadFileAPI

urlpatterns = [
    # path('', getFileList, name='getFileList'),
    path('', ListFilesView.as_view(), name='getFileList'),
    # path('upload/', fileUpload, name='fileupload')
    path('upload/', UploadFileAPI.as_view(), name='fileupload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)