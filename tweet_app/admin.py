from django.contrib import admin

from .models import TweetModel


class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_body', 'createdby', 'time_submitted']


admin.site.register(TweetModel, TweetAdmin)
