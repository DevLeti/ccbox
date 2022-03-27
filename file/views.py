from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.decorators.csrf import csrf_exempt

from .models import File

JWT_authenticator = JWTAuthentication()
@csrf_exempt
def fileUpload(request):
    if request.method == 'POST':
        user_info = JWT_authenticator.authenticate(request)
        if(user_info == None):
            return HttpResponseBadRequest("User Authorization Failed.")

        user_id=user_info[1]['user_id']
        user = User.objects.get(pk=user_id)

        url = request.FILES["uploadedFile"]
        fileupload = File(
            upload_user=user,
            url=url,
        )
        fileupload.save()
        return render(request, 'uploadsuccess.html')
    else:
        return HttpResponseNotAllowed(['POST'],content='Not Allowed Request Method.')

def getFileList(request):
    if request.method == 'GET':
        user_info = JWT_authenticator.authenticate(request)
        if (user_info == None):
            return HttpResponseBadRequest("User Authorization Failed.")

        user_id = user_info[1]['user_id']

        file_list = serializers.serialize('json', File.list.filter(upload_user=user_id))
        return HttpResponse(file_list, content_type='application/json')
    else:
        return HttpResponseNotAllowed(['POST'],content='Not Allowed Request Method.')