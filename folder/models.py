from django.db import models
from django.contrib.auth.models import User
# from file.models import File


# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_folder')
    name = models.CharField(max_length=63)