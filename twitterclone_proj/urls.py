"""twitterclone_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from twitteruser_app import views as twitteruserappview
from authentication_app import views as authenticateappview
from tweet_app import views as tweetappview

urlpatterns = [
    path('', twitteruserappview.index_view, name='homepage'),
    path('create/', tweetappview.create_tweet, name='createtweet'),
    path('login/', authenticateappview.login_view, name='loginpage'),
    path('logout/', authenticateappview.logout_view, name='logoutpage'),
    path('admin/', admin.site.urls),
]
