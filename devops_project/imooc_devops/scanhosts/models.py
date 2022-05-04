from django.db import models


# Create your models here.

class UserIPInfo(models.Model):
    ip = models.CharField(max_length=40, default="", verbose_name="IP地址", null=True)
    time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "用户访问地址信息表"
        verbose_name_plural = verbose_name
        db_table = "useripinfo"


class BrowseInfo(models.Model):
    useragent = models.CharField(max_length=150, default="", verbose_name="浏览器的agent信息", null=True)
    models.CharField(max_length=256, verbose_name="设备唯一ID", default="")

    userip = models.ForeignKey("UserIPInfo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "用户浏览器信息表"
        verbose_name_plural = verbose_name
        db_table = "browseinfo"
