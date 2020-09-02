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
        ret = self.tweet_body + ',' + self.createdby + ',' + self.time_submitted
        return ret

        class Meta:
            unique_together = ['tweet_body', 'createdby', 'time_submitted']
