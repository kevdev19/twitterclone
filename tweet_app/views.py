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


def tweet_detail_view(request, tweet_id):
    tweet_detail = TweetModel.objects.filter(id=tweet_id).first()
    return render(request, 'tweet_detail.html', {"tweet": tweet_detail})
