from django.db import models
from django.utils.timezone import now

from twitteruser_app.models import TwitterUser


class Tweet(models.Model):
    tweet_body = models.TextField(max_length=255)
    createdby = models.ForeignKey(
        TwitterUser, null=True, on_delete=models.CASCADE)
    time_submitted = models.DateTimeField(
        default=now, editable=False)

    # Displays multiple columns in admin panel
    def __str__(self):
        return self.tweet_body
