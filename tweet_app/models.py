from django.db import models
from django.utils.timezone import now

from twitteruser_app.models import TwitterUserModel


class TweetModel(models.Model):
    tweet_body = models.TextField(max_length=255)
    createdby = models.ForeignKey(
        TwitterUserModel, null=True, on_delete=models.CASCADE)
    time_submitted = models.DateTimeField(
        default=now, editable=False)

    # Displays multiple columns in admin panel
    def __str__(self):
        return self.tweet_body
