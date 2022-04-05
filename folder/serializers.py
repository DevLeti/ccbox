from rest_framework import serializers

from folder.models import Folder


class GetFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'
