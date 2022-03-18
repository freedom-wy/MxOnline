from rest_framework import serializers
from django.contrib.auth import get_user_model
from MxShopProject.settings import REGEX_MOBILE
import re
from .models import VerifyCode
from datetime import datetime


# 获取用户类
User = get_user_model()


class SmsSerializer(serializers.Serializer):
    """
    短信验证码的序列化器
    """
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号是否注册、验证手机号是否合法、验证短信发送频率
        :param mobile:
        :return:
        """
        if User.objects.filter(mobile=mobile):
            raise serializers.ValidationError("该手机号码已注册")
        elif not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码不合法")

        # 验证短信验证码发送频率
        code = VerifyCode.objects.filter(mobile=mobile)
        if code:
            exp = datetime.now() - code.first().add_time
            if exp.seconds < 60:
                raise serializers.ValidationError("距离上一次发送未超过60s")
        return mobile


