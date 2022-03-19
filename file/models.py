from django.db import models
from django.contrib.auth.models import User
# from user.models import User


# Create your models here.

class file(models.Model):
    upload_user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=511)
    allowed_users = models.ManyToManyField(User, related_name="allowed_file")
