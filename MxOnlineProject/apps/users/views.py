from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
# HttpResponseRedirect跳转
from django.http import HttpResponseRedirect
# reverse通过url中设置的name找到url
from django.urls import reverse


class IndexView(View):
    """
    首页视图
    """

    def get(self, request):
        return render(request, "index.html")


class LoginView(View):
    """
    登录视图
    """
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        # 获取从前端传递过来的用户名和密码
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 校验用户名密码是否正确
        user = authenticate(username=username, password=password)
        if user:
            # 校验成功,执行登录操作
            login(request, user)
            # 跳转到首页
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html")

