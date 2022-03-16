from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
# HttpResponseRedirect跳转
from django.http import HttpResponseRedirect
# reverse通过url中设置的name找到url
from django.urls import reverse
from .forms import LoginForm, DynamicLoginForm


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
        # 在登录页面,如果当前用户已登录则跳转到首页
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        login_form = DynamicLoginForm()
        return render(request, "login.html", {"login_form": login_form})

    def post(self, request):
        # 获取从前端传递过来的用户名和密码
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # 通过form校验前端传递过来的用户名密码数据
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            # 校验用户名密码是否正确
            user = authenticate(username=username, password=password)
            if user:
                # 校验成功,执行登录操作
                login(request, user)
                # 跳转到首页
                return HttpResponseRedirect(reverse("index"))
            else:
                # 登录校验失败
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})


class Logout(View):
    """
    退出
    """

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))
