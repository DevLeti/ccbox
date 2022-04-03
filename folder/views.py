from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from folder.models import Folder
from folder.serializers import GetFolderSerializer


class UploadFileAPI(APIView):
    serializer_class = GetFolderSerializer

    def post(self, request):
        url = request.FILES['file']
        fileupload = Folder(
            upload_user=request.user,
            url=url,
        )
        fileupload.save()
        return JsonResponse({"result": "success"})


class ListFilesView(ListAPIView):
    serializer_class = GetFolderSerializer

    def get_queryset(self):
        user_id = self.request.user
        return Folder.list.filter(upload_user=user_id)
