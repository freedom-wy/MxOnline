from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import SmsSerializer, UserRegSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import VerifyCode
from utils.random_code import generate_random
from django.contrib.auth import get_user_model
# 生成token
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

User = get_user_model()


class SmsCodeViewset(CreateModelMixin, GenericViewSet):
    """
    验证短信验证码并存储短信验证码
    """
    serializer_class = SmsSerializer

    def create(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=request.data)
        # 验证前端提交的数据
        serialzer.is_valid(raise_exception=True)

        mobile = serialzer.validated_data.get("mobile")
        # 生成验证码
        code = generate_random(4)
        # 发送验证码
        print(code)
        # 调用的是模型的save方法,不是序列化器的save方法
        save_code = VerifyCode(mobile=mobile)
        save_code.code = code
        save_code.save()
        return Response(
            {
                "mobile": mobile,
                "status": "success"
            },
            status=status.HTTP_201_CREATED
        )


class UserRegisterViewset(CreateModelMixin, GenericViewSet):
    """
    注册账号
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserRegSerializer

    # 重写create方法
    def create(self, request, *args, **kwargs):
        # 反序列化
        serializer = self.get_serializer(data=request.data)
        # 校验数据
        serializer.is_valid(raise_exception=True)
        # 数据校验通过后,保存用户数据
        user = self.perform_create(serializer)
        # # 创建token
        # token = TokenObtainPairSerializer.get_token(user=user)
        # print(token, type(token))
        token = RefreshToken.for_user(user)
        access_token = token.access_token
        response_data = serializer.data
        response_data["token"] = str(access_token)
        response_data["name"] = user.name if user.name else user.username
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        重写perform_create方法,返回user模型类
        :param serializer:
        :return:
        """
        return serializer.save()



