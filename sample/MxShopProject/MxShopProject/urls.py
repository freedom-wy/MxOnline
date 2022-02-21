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
from django.urls import path, include
# 通过django的serializers对模型类数据进行序列化并向前端返回数据
from apps.goods.views import GoodsListViewSource
from apps.goods.views import GoodsListViewDemo

urlpatterns = [
    path('admin/', admin.site.urls),
    # 仅是在api接口页面上显示一个登录按钮?
    path('api-auth/', include('rest_framework.urls')),
    # 原始json数据返回方法
    path("goods_source/", GoodsListViewSource.as_view(), name="goods_source"),
    # drf返回json数据方法
    path("goods_demo/", GoodsListViewDemo.as_view(), name="goods_demo")
]
