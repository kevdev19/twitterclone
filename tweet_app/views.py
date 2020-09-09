from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import Tweet, TwitterUser
from notification_app.models import Notification
import re
from .forms import TweetForm


# @login_required
# def create_tweet(request):
#    if request.method == "POST":
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_tweet = Tweet.objects.create(
#                 tweet_body=data.get('tweet_body'),
#                 createdby=request.user
#             )
#             mentions = re.findall(r'@(\w+)', data.get('tweet_body'))
#             if mentions:
#                 for mention in mentions:
#                     matched = TwitterUser.objects.get(username=mention)
#                     if matched:
#                         Notification.objects.create(
#                             receiver=matched, tracked_tweet=new_tweet)

#             return HttpResponseRedirect(reverse("homepage"))

#     form = TweetForm()
#     return render(request, "create_tweet.html", {"form": form})


class CreateTweetView(TemplateView):

    def get(self, request):
        form = TweetForm()
        return render(request, "create_tweet.html", {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                tweet_body=data.get('tweet_body'),
                createdby=request.user
            )
            mentions = re.findall(r'@(\w+)', data.get('tweet_body'))
            if mentions:
                for mention in mentions:
                    matched = TwitterUser.objects.get(username=mention)
                    if matched:
                        Notification.objects.create(
                            receiver=matched, tracked_tweet=new_tweet)

            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "create_tweet.html", {"form": form})


# def tweet_detail_view(request, tweet_id):
#     tweet_detail = Tweet.objects.filter(id=tweet_id).first()
#     return render(request, 'tweet_detail.html', {"tweet": tweet_detail})


class TweetDetailView(TemplateView):

    def get(self, request, tweet_id):
        tweet_detail = Tweet.objects.filter(id=tweet_id).first()
        return render(request, 'tweet_detail.html', {"tweet": tweet_detail})
