from django.db import models
from twitteruser_app.models import TwitterUser
from tweet_app.models import Tweet


class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tracked_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    read_notification = models.BooleanField(default=False)
