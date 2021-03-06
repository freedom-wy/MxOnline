from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from apps.goods.models import Goods
from utils.models_base import BaseModels

User = get_user_model()  # UserProfile


class ShoppingCart(BaseModels):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name=u"商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(BaseModels):
    """
    订单
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态")
    post_script = models.CharField(max_length=200, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    singer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(BaseModels):
    """
    订单的商品详情
    """
    # 级联删除
    """
    models.SET_NULL这里还有其他几个选项：
    * SET_NULL 当外键的字段被删除的时候设置为null前提是指定了 null=True
    * CASCADE  默认的选项，当外键关联的字段删除的时候，所有其他表级联删除
    * SET_DEFAULT 设置一个默认值，当关联的记录删除的时候恢复成默认值
    ＊DO_NOTHING　 django不做任何事情，数据库返回什么就报什么
    *  SET()还可以set一个函数，当关联记录删除的时候触发得到一个值
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单信息", related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
