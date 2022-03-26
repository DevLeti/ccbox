from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.decorators.csrf import csrf_exempt

from .forms import FileUploadForm
from .models import File


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

JWT_authenticator = JWTAuthentication()
@csrf_exempt
def fileUpload(request):
    if request.method == 'POST':
        user_info = JWT_authenticator.authenticate(request)

        user_id=user_info[1]['user_id']
        user = User.objects.get(pk=user_id)

        url = request.FILES["uploadedFile"]
        fileupload = File(
            upload_user=user,
            url=url,
        )
        fileupload.save()
        return render(request, 'uploadsuccess.html')
    # else:
    #     fileuploadForm = FileUploadForm
    #     context = {
    #         'fileuploadForm': fileuploadForm
    #     }
    #     return render(request, 'fileupload.html', context)