from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from folder.models import Folder
from folder.serializers import GetFolderSerializer


class NewFolderAPI(APIView):
    serializer_class = GetFolderSerializer

    def post(self, request):
        # TODO : get_queryset 으로 코드 간결화
        name = request.POST['name']
        try:
            parent_folder_name = request.POST['parent']
            parent_query = Folder.objects.get(name=parent_folder_name, user_id=request.user)
            new_folder = Folder(
                user=request.user,
                parent=parent_query,
                name=name,
            )
        except:
            new_folder = Folder(
                user=request.user,
                name=name,
            )

        new_folder.save()
        serializer = GetFolderSerializer(new_folder)
        return JsonResponse(serializer.data)

    def delete(self, request):
        folder_name = request.data['folder_name']
        model = Folder.objects.get(name=folder_name, user_id=request.user)
        model.delete()
        return JsonResponse({"result": "success"})




class ListFoldersAPI(ListAPIView):
    serializer_class = GetFolderSerializer

    def get_queryset(self):
        user_id = self.request.user
        return Folder.objects.filter(user_id=user_id)
