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

from twitteruser_app import views as twitteruserappviews
from authentication_app import views as authenticateappviews
from tweet_app import views as tweetappviews
from notification_app import views as notificationappviews


urlpatterns = [
    path('', twitteruserappviews.index_view, name='homepage'),
    path('tweet/<int:tweet_id>/',
         tweetappviews.TweetDetailView.as_view(), name='tweetdetail'),
    path('create/', tweetappviews.CreateTweetView.as_view(), name='createtweet'),
    path('register/', twitteruserappviews.signup_view, name='signup'),
    path('follow/<str:user_name>/',
         twitteruserappviews.follow_view, name='follow'),
    path('unfollow/<str:user_name>/',
         twitteruserappviews.unfollow_view, name='unfollow'),
    path('login/', authenticateappviews.login_view, name='loginpage'),
    path('logout/', authenticateappviews.logout_view, name='logoutpage'),
    path('admin/', admin.site.urls),
    path('notification/', notificationappviews.NotifyView.as_view(),
         name='notification'),
    path('profile/<str:user_name>/',
         twitteruserappviews.UserDetailView.as_view(), name='profilepage'),
]
