# views.py
from django.http import HttpResponse
from django.shortcuts import render

from .consumers import NotificationConsumer
from .models import Notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_notification(request):
    channel_layer = get_channel_layer()
    user_id = request.user.id  # Get the ID of the current user
    notification_data = {
        'title': 'New Notification',
        'description': 'This is a new notification message.',
    }
    async_to_sync(channel_layer.group_send)(
        f'user_{user_id}',
        {
            'type': 'notify_user',
            'notification': notification_data,
        }
    )
    # return render(request, 'notification_sent.html')


def add_notification(request):
    # if request.method == 'GET':
    #     # title = request.POST.get('title')
    #     # description = request.POST.get('description')
    #     # receiver = request.user  # Assuming the current user is the receiver
    #     notification = Notification.objects.create(
    #         title="Test",  # title,
    #         description="Test",  # description,
    #         receiver=request.user,  # receiver
    #     )
    # send_notification(request)
    return HttpResponse()


def notifications_view(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(receiver=request.user)
        return render(request, 'notifications.html', {'notifications': notifications})
    else:
        return render(request, 'notifications.html', {'notifications': []})
