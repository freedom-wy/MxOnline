from .models import Goods, GoodsCategory
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import CategorySerializer


# class GoodsListViewSet(ModelViewSet):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializerDemo
#     # 在视图中单独使用过滤器
#     filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
#     filter_fields = ["name", "goods_brief"]
#     ordering_fields = ["id", "shop_price"]
#     # 搜索
#     search_fields = ["name"]
#     # 当pagination_class为None, 该视图不分页
#     # pagination_class = None


class CategoryViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

