from django.contrib import admin
from apps.goods.models import GoodsCategory


class GoodsCategoryAdmin(admin.ModelAdmin):
    """
    自定义后台管理
    """
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


# 将自定义的后台管理注册
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
