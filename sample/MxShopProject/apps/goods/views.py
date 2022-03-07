# 未使用django rest framework向前端返回json数据方法
from django.views.generic import View
from apps.goods.models import Goods
from django.http import HttpResponse
from django.core import serializers

# 使用django rest framework向前端返回json数据方法
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GoodsSerializerDemo

# 使用generics封装serializer数据
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# 使用viewset封装serializer数据
from rest_framework import mixins, viewsets


# 使用restframework向前端提供Json数据
class GoodsApiViewSource(APIView):
    def get(self, request):
        from .serializers import GoodsSerializerDemoSource
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializerDemoSource(goods, many=True)
        return Response(data=goods_serializer.data)


class GoodsListViewSource(View):

    def get(self, request):
        # 原始方法
        # data_list = []
        # # 获取goods表内所有数据
        goods = Goods.objects.all()
        # for good in goods:
        #     data_list.append(
        #         {
        #             "name": good.name,
        #             "category": good.category.name,
        #             "market_price": good.market_price
        #         }
        #     )
        # 通过serialize方法进行序列化,使用serialize方法可以对不同数据类型数据进行序列化,序列化后直接就是json.dumps的字符串
        # serialize方法传入序列化结构和要序列化的数据
        data_list = serializers.serialize("json", goods)
        return HttpResponse(data_list, content_type="application/json")


class GoodsPagination(PageNumberPagination):
    """
    配置分页
    """
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "q"
    max_page_size = 20


class GoodsListViewDemo(generics.ListAPIView):
    """
    通过django rest framework向前端返回json数据
    """
    # def get(self, request):
    #     goods = Goods.objects.all()
    #     # goods为列表数据,在GoodsSerializerDemo中需要配置many
    #     goods_serializer = GoodsSerializerDemo(goods, many=True)
    #     return Response(goods_serializer.data)

    # 使用generics.ListAPIView后不需要重写get方法,只需实例化取出models数据和传入serializer类即可
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializerDemo
    # 调用分页配置后前端可以通过http://127.0.0.1:8000/goods_demo/?q=1&page_size=20访问
    pagination_class = GoodsPagination


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    使用viewset封装serializer数据
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializerDemo
    pagination_class = GoodsPagination
