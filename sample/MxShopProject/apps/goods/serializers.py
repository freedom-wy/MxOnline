from rest_framework import serializers


class GoodsSerializerDemo(serializers.Serializer):
    """
    商品数据序列化demo
    """
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)



