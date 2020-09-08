from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


from tweet_app.models import Tweet, TwitterUser

from .forms import RegistrationForm


@login_required
def index_view(request):
    tweets = Tweet.objects.all().order_by('-time_submitted')
    following = request.user.followers.all()
    return render(request, 'index.html', {"tweets": tweets})


def signup_view(request):
    if request.method == 'POST':
        signup_form = RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('homepage')

    else:
        signup_form = RegistrationForm()

    return render(request, 'signup.html', {"form": signup_form})


def user_detail_view(request, user_name):
    profile = TwitterUser.objects.filter(username=user_name).first()
    tweets = Tweet.objects.filter(
        createdby=profile).order_by('-time_submitted')
    if request.user.is_authenticated:
        followers = request.user.followers.all()
    else:
        followers = []
    return render(request, 'user_detail.html', {"profile": profile, "tweets": tweets, "followers": followers})


def follow_view(request, user_name):
    current_user = request.user
    following_user = TwitterUser.objects.filter(
        username=user_name).first()
    current_user.followers.add(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def unfollow_view(request, user_name):
    current_user = request.user
    following_user = TwitterUser.objects.filter(
        username=user_name).first()
    current_user.followers.remove(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
