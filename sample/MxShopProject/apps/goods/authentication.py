from rest_framework.authentication import BaseAuthentication
# from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class CustomAuthentication(BaseAuthentication):
    """
    自定义认证方案
    """
    def authenticate(self, request):
        username = request.query_params.get("user")
        password = request.query_params.get("pwd")
        # user = get_user_model().object.first()
        # 验证登录用户
        user = authenticate(username=username, password=password)
        return user, None

