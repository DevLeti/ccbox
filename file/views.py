from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from folder.models import Folder
from folder.views import ListFoldersAPI
from .models import File
from .serializers import GetFileSerializer


class UploadFileAPI(APIView):
    serializer_class = GetFileSerializer

    def post(self, request):
        url = request.FILES['file']
        file_name = request.data['file_name']
        folder = Folder.objects.get(user_id=request.user, name=request.data['folder'])
        fileupload = File(
            upload_user=request.user,
            url=url,
            file_name=file_name,
            folder=folder
        )
        fileupload.save()
        return JsonResponse({"result": "success"})

    def delete(self, request):
        file_name = request.data['file_name']
        folder = Folder.objects.get(user_id=request.user, name=request.data['folder'])
        print(folder)
        model = File.objects.get(file_name=file_name, folder=folder, upload_user=request.user)
        model.delete()
        return JsonResponse({"result": "success"})



class ListFilesAPI(ListAPIView):
    serializer_class = GetFileSerializer

    def get_queryset(self):
        user_id = self.request.user
        return File.objects.filter(upload_user=user_id)
