from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


from tweet_app.models import TweetModel, TwitterUserModel

from .forms import RegistrationForm


@login_required
def index_view(request):
    tweets = TweetModel.objects.all()
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
    user_detail = TwitterUserModel.objects.get(username=user_name)
    return render(request, 'user_detail.html', {"user_detail": user_detail})
