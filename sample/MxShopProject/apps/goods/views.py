from .serializers import GoodsSerializerDemo
from .models import Goods
from rest_framework import status
from .authentication import CustomAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class GoodsListViewSet(ModelViewSet):
    # 自定义认证方案
    # authentication_classes = [CustomAuthentication]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializerDemo

    def list(self, request, *args, **kwargs):
        if not request.user:
            return Response("未登录用户")
        else:
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
