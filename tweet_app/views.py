from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from .models import TweetModel, TwitterUserModel

from .forms import TweetForm


def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = TweetModel.objects.create(
                tweet_body=data.get('tweet_body'),
                createdby=request.user
            )
            if new_tweet:
                return HttpResponseRedirect(reverse("homepage"))

    form = TweetForm()
    return render(request, "create_tweet.html", {"form": form})
