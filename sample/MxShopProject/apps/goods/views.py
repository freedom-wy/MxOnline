from .models import Goods, GoodsCategory
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import CategorySerializer, GoodsSerializer
from .filters import GoodsFilter
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    # 每页显示条目
    page_size = 12
    # 分页大小
    page_size_query_param = "page_size"
    # 页码
    page_query_param = "page"
    # 最大页码
    max_page_size = 100


class GoodsListViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 调用自定义过滤器,使用自定义过滤器时需引入DjangoFilterBackend
    filter_class = GoodsFilter
    # 在视图中单独使用过滤器
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    # 排序
    ordering_fields = ['sold_num', 'shop_price']
    # 搜索
    search_fields = ["name", 'goods_brief', 'goods_desc']
    # 分页
    pagination_class = GoodsPagination

    # 使用默认过滤器时定义可过滤字段
    # filter_fields = ["name", "goods_brief"]

    # 当pagination_class为None, 该视图不分页
    # pagination_class = None


class CategoryViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class AuthDemo(ListModelMixin, GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # authentication_classes = [SessionAuthentication]

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response
        print(request.user)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

