# 模型类基类
from django.db import models
from django.utils.timezone import now


class BaseModels(models.Model):
    add_time = models.DateTimeField(default=now, verbose_name="添加时间")

    # 不创建基类表
    class Meta:
        abstract = True
