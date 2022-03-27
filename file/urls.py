from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import fileUpload, getFileList

urlpatterns = [
    path('', getFileList, name='getFileList'),
    path('upload/', fileUpload, name='fileupload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)