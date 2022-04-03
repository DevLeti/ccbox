from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from folder.models import Folder
from folder.serializers import GetFolderSerializer


class NewFolderAPI(APIView):
    serializer_class = GetFolderSerializer

    def post(self, request):
        parent_string = request.POST['parent']
        parent_query = Folder.objects.get(name=parent_string)
        print(parent_query)
        name = request.POST['name']
        fileupload = Folder(
            user=request.user,
            parent=parent_query,
            name=name,
        )
        fileupload.save()
        return JsonResponse({"result": "success"})


class ListFoldersView(ListAPIView):
    serializer_class = GetFolderSerializer

    def get_queryset(self):
        user_id = self.request.user
        return Folder.objects.filter(user_id=user_id)
