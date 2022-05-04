from django.urls import re_path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    re_path("^ws/chat/(?P<room_name>[^/]+)/$", ChatConsumer.as_asgi())
]



