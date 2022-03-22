from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from .serializers import UserFavSerializers
from .models import UserFav
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


# Create your views here.


class UserFavViewset(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    """
    list：获取用户收藏列表
    retrieve：判断某个商品是否已经收藏
    create：收藏商品
    """
    serializer_class = UserFavSerializers
    # IsOwnerOrReadOnly用于判定当前请求用户和模型中用户是否为同一个, IsAuthenticated用于判定当前请求是否已登录
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # SessionAuthentication用于web界面api接口, jwt用于postman中api接口
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):
        """
        根据用户返回其收藏数据
        :return:
        """
        return UserFav.objects.filter(user=self.request.user)
