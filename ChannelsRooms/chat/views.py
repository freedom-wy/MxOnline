from django.shortcuts import render
from django.views import View
from django.utils.safestring import mark_safe
import json


# Create your views here.


class ChatIndexView(View):
    def get(self, request):
        return render(request, "chat/index.html")


class ChatRoomView(View):
    def get(self, request, room_name):
        return render(request, "chat/room.html", {"room_name_json": mark_safe(json.dumps(room_name))})
