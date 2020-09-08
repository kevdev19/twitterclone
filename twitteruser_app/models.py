from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    displayname = models.CharField(max_length=60, null=False)
    bio = models.TextField(max_length=255, default='Bio')
    website = models.URLField(max_length=255, default='http://mywebsite.com')
    followers = models.ManyToManyField('self', symmetrical=False,
                                       blank=True)

    def __str__(self):
        return self.username
