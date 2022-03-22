from django.contrib import admin
from .models import UserFav

# Register your models here.


class UserFavAdmin(admin.ModelAdmin):
    """
    用户收藏后台管理
    """
    list_display = ['user', 'goods']


admin.site.register(UserFav, UserFavAdmin)



