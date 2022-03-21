from rest_framework import serializers
from django.contrib.auth import get_user_model
from MxShopProject.settings import REGEX_MOBILE
import re
from .models import VerifyCode
from datetime import datetime
from rest_framework.validators import UniqueValidator

# 获取用户类
User = get_user_model()


class SmsSerializer(serializers.Serializer):
    """
    短信验证码的序列化器
    """
    mobile = serializers.CharField(max_length=11, label="手机号码")

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


class UserRegSerializer(serializers.ModelSerializer):
    # 添加一个模型类中没有的字段,write_only仅进行反序列化操作,不进行序列化操作
    code = serializers.CharField(required=True, max_length=4, min_length=4, help_text="验证码", write_only=True)
    # message是validator中的参数
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")],
                                     required=True, allow_blank=False, help_text="用户名")
    # style将drf接口中提交数据样式设置为圆点
    password = serializers.CharField(help_text="密码", style={"input_type": "password"}, write_only=True)

    # 反序列化时数据校验
    def validate_code(self, code):
        # 校验验证码
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data.get("username"))
        if verify_records:
            records = verify_records.first()

            # 检查验证码是否过期
            exp = datetime.now() - records.add_time
            # 大于5分钟
            if exp.seconds > 5 * 60:
                raise serializers.ValidationError("验证码已过期")
            elif records.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        # code验证通过后即可删除,无需保存到user表中
        del attrs["code"]
        attrs["mobile"] = attrs["username"]
        return attrs

    def create(self, validated_data):
        """
        调用父类的create方法
        :param validated_data:
        :return:
        """
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "password", "code"]
