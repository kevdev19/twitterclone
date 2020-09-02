from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from tweet_app.models import TweetModel, TwitterUserModel


@login_required
def index_view(request):
    tweets = TweetModel.objects.all()
    return render(request, 'index.html', {"tweets": tweets})
