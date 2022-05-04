from django.db import models


# Create your models here.

# 注释掉demo模型类
# class UserIPInfo(models.Model):
#     ip = models.CharField(max_length=40, default="", verbose_name="IP地址", null=True)
#     time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
#
#     class Meta:
#         verbose_name = "用户访问地址信息表"
#         verbose_name_plural = verbose_name
#         db_table = "useripinfo"
#
#
# class BrowseInfo(models.Model):
#     useragent = models.CharField(max_length=150, default="", verbose_name="浏览器的agent信息", null=True)
#     models.CharField(max_length=256, verbose_name="设备唯一ID", default="")
#
#     userip = models.ForeignKey("UserIPInfo", on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "用户浏览器信息表"
#         verbose_name_plural = verbose_name
#         db_table = "browseinfo"

class HostLogininfo(models.Model):
    """
    设备登录信息
    """

    ip = models.CharField(max_length=64, null=False, blank=False, verbose_name="设备IP地址")
    # null设置为true时,当该字段为空时,django会将数据库中该字段设置为NULL
    # blank设置为true时,允许该字段为空
    ssh_port = models.CharField(max_length=32, null=True, blank=True, verbose_name="SSH登录端口")
    ssh_user = models.CharField(max_length=32, null=True, blank=True, verbose_name="SSH登录用户")
    ssh_password = models.CharField(max_length=64, null=True, blank=True, verbose_name="SSH登录密码")
    ssh_rsa = models.CharField(max_length=64, null=True, blank=True, verbose_name="ssh私钥")
    rsa_password = models.CharField(max_length=64, null=True, blank=True, verbose_name="私钥的密码")
    ssh_status = models.IntegerField(verbose_name="0-登录失败,1-登录成功", default=0)
    ssh_type = models.IntegerField(verbose_name="1-rsa登录,2-dsa登录,3-普通用户rsa登录,4-docker成功,5-docker无法登录", default=0)
    system_version = models.CharField(max_length=256, null=True, blank=True, verbose_name="操作系统版本")
    hostname = models.CharField(max_length=256, null=True, blank=True, verbose_name="主机名")
    mac_adddress = models.CharField(max_length=512, null=True, blank=True, verbose_name="MAC地址")
    sn = models.CharField(max_length=256, null=True, blank=True, verbose_name="设备SN号码")
    machine_type = models.IntegerField(verbose_name="机器的类型 1=物理服务器,2=虚拟资产,3=网络设备 0=其他类型(未知)", default=0)
    physics_machine_type = models.CharField(max_length=256, verbose_name="虚拟机上宿主机的类型")

    class Meta:
        verbose_name = "初始化扫描信息表"
        verbose_name_plural = verbose_name
        db_table = "hostlogininfo"




