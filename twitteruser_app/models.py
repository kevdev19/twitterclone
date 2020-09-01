from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUserModel(AbstractUser):
    displayname = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.username
