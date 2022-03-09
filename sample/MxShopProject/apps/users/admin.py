from django.contrib import admin
from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin

# 直接注册默认的管理员
admin.site.register(UserProfile, UserAdmin)
