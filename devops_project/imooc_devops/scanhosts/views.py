from django.shortcuts import render
from django.views.generic.base import View
from .models import UserIPInfo, BrowseInfo
from django.http import JsonResponse


# Create your views here.

class UserInfoView(View):
    """
    采集用户信息
    """

    def get(self, request):
        ip_addr = request.META.get("REMOTE_ADDR")
        user_ua = request.META.get("HTTP_USER_AGENT")

        user_obj = UserIPInfo.objects.filter(ip=ip_addr)
        if not user_obj:
            res = UserIPInfo.objects.create(ip=ip_addr)
            ip_addr_id = res.id
        else:
            ip_addr_id = user_obj.first().id

        BrowseInfo.objects.create(useragent=user_ua, userip_id=ip_addr_id)
        content = {
            "STATUS": "success",
            "INFO": "User info",
            "IP": ip_addr,
            "UA": user_ua
        }
        return JsonResponse(data=content, status=200)
