from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from action import consumers
from action.consumers import ActionConsumer

websocket_urlpatterns = [
    re_path(r'action/accessrecord/(?P<building_id>\d+)/$', ActionConsumer.as_asgi()),
]
