from django.shortcuts import render


# 未使用django rest framework向前端返回json数据方法
from django.views.generic import View
from apps.goods.models import Goods
import json
from django.http import HttpResponse
from django.core import serializers


class GoodsListView(View):

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

