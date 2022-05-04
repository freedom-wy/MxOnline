"""Message URL Configuration

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
# from django.contrib import admin
from django.urls import path
from apps.message_form1.views import message_views
from apps.message_form1.views import ShotGetMessage, ShotPostMessage, LongCreateMessage, LongGetMessage, LongPostMessage
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 短轮询
    path("shot_get/", ShotGetMessage.as_view(), name="get_message"),
    path("shot_post/", ShotPostMessage.as_view(), name="post_message"),
    # 长轮询
    path("create_room/", LongCreateMessage.as_view(), name="long_create"),
    path("long_get/", LongGetMessage.as_view(), name="long_get"),
    path("long_post/", LongPostMessage.as_view(), name="long_post"),
    # 添加应用的url和视图函数
    path('', message_views)
]
