from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
# HttpResponseRedirect跳转
from django.http import HttpResponseRedirect, JsonResponse
# reverse通过url中设置的name找到url
from django.urls import reverse
from .forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm, RegisterGetForm, RegisterPostForm
from utils.random_code import generate_random
from apps.users.models import PhoneCode, UserProfile


class IndexView(View):
    """
    首页视图
    """

    def get(self, request):
        return render(request, "index.html")


class DynamicLoginView(View):
    """
    手机验证码登录视图
    """
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        # 展示验证码
        login_form = DynamicLoginForm()
        return render(request, "login.html", {"login_form": login_form})

    def post(self, request):
        login_form = DynamicLoginPostForm(request.POST)
        dynami_login = True
        if login_form.is_valid():
            mobile = login_form.cleaned_data.get("mobile")
            # 查询用户表是否有该手机号,如果有则登录,如果没有则注册
            existed_users = UserProfile.objects.filter(mobile=mobile)
            if existed_users:
                user = existed_users.first()
            else:
                # 注册账号
                user = UserProfile(username=mobile)
                # 生成随机密码
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # 手机验证码登录校验失败
            d_form = DynamicLoginForm()
            return render(request, "login.html", {
                "login_form": login_form,
                "d_form": d_form,
                "dynamic_login": dynami_login
            })


class LoginView(View):
    """
    传统的用户名密码登录视图
    """

    def get(self, request):
        # 在登录页面,如果当前用户已登录则跳转到首页
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        # 展示验证码
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


class SendSmsView(View):
    """
    发送短信验证码和校验图片验证码
    """
    def post(self, request):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            # 生成验证码并发送
            sms_code = generate_random(4)
            # 模拟发送手机短信,永远发送成功
            print(sms_code)
            # 存储短信验证码,用于校验,此处使用redis最方便
            # save_sms_code = PhoneCode(phone_num=send_sms_form.cleaned_data.get("mobile"), phone_code=sms_code)
            save_sms_code = PhoneCode()
            save_sms_code.phone_num = send_sms_form.cleaned_data.get("mobile")
            save_sms_code.phone_code = sms_code
            save_sms_code.save()
            re_dict["status"] = "success"
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]
        return JsonResponse(re_dict)


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        register_get_form = RegisterGetForm()
        return render(request, "register.html", {"register_get_form": register_get_form})

    def post(self, request):
        register_post_form = RegisterPostForm(request.POST)
        if register_post_form.is_valid():
            mobile = register_post_form.cleaned_data.get("mobile")
            password = register_post_form.cleaned_data.get("password")
            # 创建用户
            user = UserProfile(username=mobile, mobile=mobile)
            user.set_password(password)
            user.save()
            # 登录
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            register_get_form = RegisterGetForm()
            return render(request, "register.html", {
                "register_get_form": register_get_form,
                "register_post_form": register_post_form
            })



