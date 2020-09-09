from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import Tweet, TwitterUser, Notification


# @login_required
# def notify(request):
#     notifications = Notification.objects.filter(receiver=request.user)
#     notification_count = 0
#     new_notifications = []
#     for notification in notifications:
#         if notification.read_notification == False:
#             new_notifications.append(notification.tracked_tweet)
#             notification.read_notification = True
#             notification_count += 1
#             notification.save()
#     return render(request, 'notification.html', {"new": new_notifications, "count": notification_count})


class NotifyView(TemplateView):

    def get(self, request):
        notifications = Notification.objects.filter(receiver=request.user)
        notification_count = 0
        new_notifications = []
        for notification in notifications:
            if notification.read_notification == False:
                new_notifications.append(notification.tracked_tweet)
                notification.read_notification = True
                notification_count += 1
                notification.save()
        return render(request, 'notification.html', {"new": new_notifications, "count": notification_count})
