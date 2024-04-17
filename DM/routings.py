from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from action import consumers

websocket_urlpatterns = [
    path('action/accessrecord/', consumers.ActionConsumer.as_asgi()),
]
