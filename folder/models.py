from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_folder', null=True)
    name = models.CharField(max_length=63)
    color = models.IntegerField(default=0)

    objects = models.Manager()
