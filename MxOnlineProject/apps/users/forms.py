# 通过form进行验证
from django import forms


class LoginForm(forms.Form):
    """
    登录form校验
    """
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)

