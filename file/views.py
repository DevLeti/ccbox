from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework_simplejwt.authentication import JWTAuthentication

from .forms import FileUploadForm
from .models import File


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

JWT_authenticator = JWTAuthentication()
def fileUpload(request):
    if request.method == 'POST':
        # response = JWT_authenticator.authenticate(request)
        # print(response)
        url = request.FILES["uploadedFile"]
        fileupload = File(
            url=url,
        )
        fileupload.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm
        }
        return render(request, 'fileupload.html', context)