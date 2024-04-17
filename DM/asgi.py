import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from .routings import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DM.settings')

# 配置 ProtocolTypeRouter
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),  # routing(urls), consumers(view)
})
