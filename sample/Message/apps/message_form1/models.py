from django.db import models


# Create your models here.


class Base(models.Model):
    """
    模型类基类
    """
    create_time = models.DateTimeField(verbose_name="留言时间", auto_now=True)
    status = models.BooleanField(verbose_name="是否删除", default=True)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)

    class Meta:
        abstract = True


class Message(Base):
    """
    创建留言板的表结构
    """
    name = models.CharField(max_length=20, verbose_name="姓名")
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.TextField(verbose_name="留言信息")

    class Meta:
        """
        这张表的一些信息
        """
        verbose_name = "留言信息"
        verbose_name_plural = verbose_name
        # 表名
        db_table = "message"
