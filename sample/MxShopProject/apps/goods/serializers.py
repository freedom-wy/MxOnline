from rest_framework import serializers
from apps.goods.models import Goods, GoodsCategory


class GoodsSerializerDemoSource(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    goods_brief = serializers.CharField(max_length=500)
    goods_front_image = serializers.ImageField()


class CategorySerializerDemo(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 通过ModelSerializer直接序列化Model数据
class GoodsSerializerDemo(serializers.ModelSerializer):
    """
    商品数据序列化demo
    """
    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)

    # 将goods中category外键显示出来
    category = CategorySerializerDemo()

    class Meta:
        model = Goods
        # 限定输出字段
        # fields = ("name", "click_num", "add_time")
        # 显示所有字段
        fields = "__all__"
