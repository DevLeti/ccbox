from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from folder.models import Folder
from folder.serializers import GetFolderSerializer


class NewFolderAPI(APIView):
    serializer_class = GetFolderSerializer

    def post(self, request):
        # TODO : get_queryset 으로 코드 간결화
        parent_string = request.POST['parent']
        parent_query = Folder.objects.get(name=parent_string)
        name = request.POST['name']
        fileupload = Folder(
            user=request.user,
            parent=parent_query,
            name=name,
        )
        fileupload.save()

        serializer = GetFolderSerializer(fileupload)
        return JsonResponse(serializer.data)


class ListFoldersAPI(ListAPIView):
    serializer_class = GetFolderSerializer

    def get_queryset(self):
        user_id = self.request.user
        return Folder.objects.filter(user_id=user_id)
