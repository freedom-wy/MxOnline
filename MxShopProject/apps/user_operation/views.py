from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, RetrieveModelMixin
from .serializers import UserFavSerializers
from .models import UserFav


# Create your views here.


class UserFavViewset(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    """
    list：获取用户收藏列表
    retrieve：判断某个商品是否已经收藏
    create：收藏商品
    """
    serializer_class = UserFavSerializers
    queryset = UserFav.objects.all()

