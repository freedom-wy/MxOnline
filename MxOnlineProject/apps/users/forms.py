# 通过form进行验证
from django import forms
from captcha.fields import CaptchaField
from .models import PhoneCode, UserProfile
import datetime


class LoginForm(forms.Form):
    """
    登录form校验
    """
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


class DynamicLoginForm(forms.Form):
    """
    动态图片验证码和手机号校验get请求
    """
    # 图片验证码
    captcha = CaptchaField()
    # 手机号
    mobile = forms.CharField(required=True, min_length=11, max_length=11)


class DynamicLoginPostForm(forms.Form):
    """
    短信验证码登录时校验,post请求
    """
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        """
        对手机验证码进行校验
        :return:
        """
        mobile = self.data.get("mobile")
        code = self.data.get("code")
        code_info = PhoneCode.objects.filter(phone_num=mobile, phone_code=code)
        if not code_info:
            raise forms.ValidationError("验证码不正确")
        else:
            code_info = code_info.first()
            now = datetime.datetime.now()
            exp_value = now - code_info.add_time
            if exp_value.seconds > 5*60:
                raise forms.ValidationError("验证码已过期")
            return code


class RegisterPostForm(DynamicLoginPostForm):
    password = forms.CharField(required=True, min_length=10)

    def clean_mobile(self):
        mobile = self.data.get("mobile")
        # 验证该手机号码是否已注册
        users = UserProfile.objects.filter(mobile=mobile)
        if users:
            raise forms.ValidationError("该手机号码已注册")
        return mobile


