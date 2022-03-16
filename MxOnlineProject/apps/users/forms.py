# 通过form进行验证
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    登录form校验
    """
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    """
    动态图片验证码和手机号校验
    """
    # 图片验证码
    captcha = CaptchaField()
    # 手机号
    mobile = forms.CharField(required=True, min_length=11, max_length=11)

