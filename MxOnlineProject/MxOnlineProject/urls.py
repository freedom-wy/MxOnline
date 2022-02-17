"""MxOnlineProject URL Configuration

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
from django.urls import path
# 导入视图
from apps.users.views import LoginView, IndexView

urlpatterns = [
    # django默认的原始的管理后台
    path('admin/', admin.site.urls),
    # name用于给html中url设定的名称
    path("", IndexView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login")
]
