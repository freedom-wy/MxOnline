from django.urls import path, re_path
from .views import ChatIndexView, ChatRoomView


urlpatterns = [
    path("", ChatIndexView.as_view(), name="index"),
    re_path("^(?P<room_name>[^/]+)/$", ChatRoomView.as_view(), name="room")
]

