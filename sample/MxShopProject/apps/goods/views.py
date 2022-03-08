from .serializers import GoodsSerializerDemo
from .models import Goods
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class GoodsListViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializerDemo
    # 在视图中单独使用过滤器
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ["name", "goods_brief"]
    ordering_fields = ["id", "shop_price"]
    # 当pagination_class为None, 该视图不分页
    # pagination_class = None

