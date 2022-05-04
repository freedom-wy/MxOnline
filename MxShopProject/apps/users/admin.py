from django.contrib import admin
from apps.users.models import UserProfile, VerifyCode
from django.contrib.auth.admin import UserAdmin


class VerifyCodeAdmin(admin.ModelAdmin):
    pass


# 直接注册默认的管理员
admin.site.register(UserProfile, UserAdmin)
admin.site.register(VerifyCode, VerifyCodeAdmin)
