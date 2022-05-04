"""MxShopProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from apps.goods.views import CategoryViewset, GoodsListViewSet
from apps.users.views import SmsCodeViewset, UserRegisterViewset
from apps.user_operation.views import UserFavViewset
# 显示商品图片
from MxShopProject.settings import MEDIA_ROOT
from django.views.static import serve
# jwt验证
from rest_framework_simplejwt.views import TokenObtainPairView

# 实例化路由并注册
router = DefaultRouter()
# 商品分类
router.register("categorys", CategoryViewset, basename="categorys")
# 商品
router.register("goods", GoodsListViewSet, basename="goods")
# 短信验证码
router.register("code", SmsCodeViewset, basename="code")
# 用户注册
router.register("users", UserRegisterViewset, basename="register")
# 用户收藏
router.register("userfavs", UserFavViewset, basename="userfavs")

urlpatterns = [
    # django原生的admin管理后台
    path('admin/', admin.site.urls),
    # 仅是在api接口页面上显示一个登录按钮?
    path('api-auth/', include('rest_framework.urls')),
    # jwt验证
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # 商品图片路由
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path("", include(router.urls))
]
# print(router.urls)
