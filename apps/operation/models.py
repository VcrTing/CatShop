from django.db import models
from apps.user.models import *
from apps.product.models import Product
from apps.web_config import *
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    order_code = models.CharField(max_length=100, verbose_name=u"订单号")
    address = models.TextField(verbose_name=u"收货地址")
    post = models.CharField(max_length=100, verbose_name=u"邮政编码")
    receiver = models.CharField(max_length=100, verbose_name=u"收货人信息")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号码")
    user_msg = models.TextField(verbose_name=u"用户备注信息")
    create_time = models.DateTimeField(verbose_name=u"创建日期", default=timezone.now)
    pay_time = models.DateTimeField(verbose_name=u"支付日期", default=timezone.now)
    delivery_time = models.DateTimeField(verbose_name=u"发货日期", default=timezone.now)
    confirm_time = models.DateTimeField(verbose_name=u"确认收货日期", default=timezone.now)
    status = models.CharField(choices=(("waitPay", u"等待支付"),
                                       ("waitDelivery", u"等待发货"),
                                       ("waitConfirm", u"等待收货"),
                                       ("finish", u"交易完成"),
                                       ("delete", u"订单删除"),
                                       ), default="waitPay",
                              max_length=100, verbose_name=u"订单状态")
    user = models.ForeignKey(UserAccount, verbose_name=u"用户", on_delete=models.SET_NULL, blank=True, null=True)
    product_id = models.IntegerField(verbose_name='产品id',blank=True, null=True)
    data_status = models.IntegerField(verbose_name='数据状态', blank=True, default=1)

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def get_order_item(self):
        return self.orderitem_set.all()

    def get_order_count(self):
        return self.orderitem_set.all().count()

    def get_order_item_id(self):
        return self.get_order_item_id()

    def __str__(self):
        return self.order_code

class OrderItem(models.Model):
    number = models.IntegerField(verbose_name=u"购买数量")
    product = models.ForeignKey(Product, verbose_name=u"产品", on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, verbose_name="订单", on_delete=models.SET_NULL, blank=True, null=True) # 没有订单时为null
    user_account = models.ForeignKey(UserAccount, verbose_name="用户", on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(choices=(("default", u"初始状态"),
                                       ("confirm", u"货物派发中"),
                                       ("waitReview", u"等待评价"),
                                       ("finish", u"交易完成")),
                              max_length=20, verbose_name=u"订单项状态", default="default")
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now())
    data_status = models.IntegerField(verbose_name='数据状态', default=1)
    order_code = models.CharField(verbose_name='订单编号', max_length=249, null=True, blank=True)

    class Meta:
        verbose_name = u"订单项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)