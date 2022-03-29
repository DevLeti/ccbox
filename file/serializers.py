from rest_framework import serializers

from file.models import File


class GetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
