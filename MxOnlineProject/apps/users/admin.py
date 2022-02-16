from django.contrib import admin
from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin


class UserProfileAdmin(admin.ModelAdmin):
    pass


# 在admin后台管理中注册
admin.site.register(UserProfile, UserAdmin)
