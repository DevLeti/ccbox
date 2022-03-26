from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import fileUpload

urlpatterns = [
    path('', views.index, name='index'),
    path('fileupload/', fileUpload, name='fileupload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)