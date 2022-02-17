from django.contrib import admin
from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin import views


# # 管理后台全局设置
# class GlobalSettings(object):
#     site_title = "在线教育平台管理后台"
#     site_footer = "yase.me"


class UserProfileAdmin(admin.ModelAdmin):
    pass


# 在admin后台管理中注册
admin.site.register(UserProfile, UserAdmin)

# # 将全局设置注册到管理后台
# admin.site.register(views.CommAdminView)
