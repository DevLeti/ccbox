from django.db import models
from django.contrib.auth.models import User
from folder.models import Folder


class File(models.Model):
    upload_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)
    url = models.FileField(upload_to="")
    allowed_users = models.ManyToManyField(User, related_name="allowed_file", null=True)

    list = models.Manager()

    def as_dict(self):
        return {
            "id": self.id,
            "upload_user": self.upload_user,
            "url": self.url,
            "allowed_users": self.allowed_users
        }