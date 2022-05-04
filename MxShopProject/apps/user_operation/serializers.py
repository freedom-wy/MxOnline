# 和用户操作相关的序列化器,如用户收藏等
from rest_framework import serializers
from .models import UserFav
from rest_framework.validators import UniqueTogetherValidator


class UserFavSerializers(serializers.ModelSerializer):
    # 取当前已登录用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        # 创建联合索引
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]
        # 显示收藏表的Id
        fields = ["user", "goods", "id"]
