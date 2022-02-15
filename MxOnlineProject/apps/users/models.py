from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


# 用户表
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # null和blank设置相关字段为空
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 通过手机号注册,不能为空,不能重复
    mobile = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    # upload_to设置图片上传后上传位置,相对media的子路径, default设置默认头像
    image = models.ImageField(upload_to="head_image/%Y/%m", verbose_name="头像", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name if self.nick_name else self.username
