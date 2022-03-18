from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import SmsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import VerifyCode
from utils.random_code import generate_random

# Create your views here.


class SmsCodeViewset(CreateModelMixin, GenericViewSet):
    """
    验证短信验证码并存储短信验证码
    """
    serializer_class = SmsSerializer

    def create(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)

        mobile = serialzer.validated_data.get("mobile")
        # 生成验证码
        code = generate_random(4)
        # 发送验证码
        print(code)
        save_code = VerifyCode(code=code, mobile=mobile)
        save_code.save()
        return Response(
            {
                "mobile": mobile,
                "status": "success"
            },
            status=status.HTTP_201_CREATED
        )



