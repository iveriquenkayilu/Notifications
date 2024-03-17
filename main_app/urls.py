# routing.py
from django.urls import re_path
from . import consumers
from django.contrib import admin
from django.urls import path
from .views import *

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]

urlpatterns = [
    path('post/', add_notification, name='add_notification'),
    path('notifications/', notifications_view, name='notifications'),
]
