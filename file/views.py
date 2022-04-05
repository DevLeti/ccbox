from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import File
from .serializers import GetFileSerializer


class UploadFileAPI(APIView):
    serializer_class = GetFileSerializer

    def post(self, request):
        url = request.FILES['file']
        fileupload = File(
            upload_user=request.user,
            url=url,
        )
        fileupload.save()
        return JsonResponse({"result": "success"})


class ListFilesAPI(ListAPIView):
    serializer_class = GetFileSerializer

    def get_queryset(self):
        user_id = self.request.user
        return File.objects.filter(upload_user=user_id)
