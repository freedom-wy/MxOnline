from django.shortcuts import render
from apps.message_form1.models import Message
from django.views import View
from django.http import JsonResponse
import json
from queue import Queue


# Create your views here.

def message_views(request):
    if request.method == "POST":
        if request.POST.get("name"):
            message_data = Message()
            # message_data.name = request.POST.get("name")
            # message_data.email = request.POST.get("email")
            # message_data.address = request.POST.get("address")
            # message_data.message = request.POST.get("message")
            message_data.set_attrs(request.POST)
            message_data.save()
    return render(request, "message_form.html")


message_list = []
message_queue_dict = {}


class ShotGetMessage(View):
    def get(self, request):
        """
        获取消息
        :param request:
        :return:
        """
        index = int(request.GET.get("index"))
        data = message_list[index:]
        return JsonResponse({"message": data})


class ShotPostMessage(View):
    def post(self, request):
        """
        发送消息
        :param request:
        :return:
        """
        post_data = request.body.decode("utf-8")
        append_data = json.loads(post_data)
        message_list.append(append_data)
        return JsonResponse({"message": "消息发送成功"})


class LongCreateMessage(View):
    def get(self, request):
        """
        创建聊天室
        :param request:
        :return:
        """
        uid = request.GET.get("uid")
        message_queue_dict[uid] = Queue()
        return JsonResponse({"message": "聊天室创建成功"}, status=201)


class LongGetMessage(View):
    def get(self, request):
        """
        获取长轮询数据
        :param request:
        :return:
        """
        uid = request.GET.get("uid")
        data = ""
        try:
            q_uid = message_queue_dict.get(uid)
            if q_uid:
                data = q_uid.get(timeout=5)
        except Exception as e:
            return JsonResponse({"message": data}, status=400)
        else:
            return JsonResponse({"message": data}, status=200)


class LongPostMessage(View):
    def post(self, request):
        """
        向所有队列中发送数据
        :param request:
        :return:
        """
        post_data = request.body.decode("utf-8")
        for k, v in message_queue_dict.items():
            v.put(post_data)
        return JsonResponse({"message": "发送数据成功"}, status=200)
