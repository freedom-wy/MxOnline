from django.shortcuts import render
from django.views.generic.base import View


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
        pass
