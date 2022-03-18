from rest_framework import serializers
from apps.goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 通过ModelSerializer直接序列化Model数据
class GoodsSerializer(serializers.ModelSerializer):
    """
    商品数据序列化
    """

    # 将goods中category外键显示出来
    category = CategorySerializer()

    class Meta:
        model = Goods
        # 限定输出字段
        # fields = ("name", "click_num", "add_time")
        # 显示所有字段
        fields = "__all__"
