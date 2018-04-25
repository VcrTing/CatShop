from django.db import models
from django.utils import timezone

# Create your models here.

# 网站信息
class WebMessage(models.Model):
    register_num = models.CharField(verbose_name='注册人数', max_length=200, default='猫之商城')
    oline_num = models.CharField(verbose_name='在线人数', max_length=200, default='猫之商城')
    site_running_time = models.DateTimeField(verbose_name='站点开始运行的时间', auto_now_add=True)
    site_front_status = models.NullBooleanField(verbose_name='前台站点开启状态', default=True)
    site_message = models.CharField(verbose_name='站点全局信息', max_length=250, default='无')

    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"站点相关"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '站点情况'

# 二维码通信商家
class Business(models.Model):
    business_id = models.CharField(verbose_name='商家id', max_length=200, blank=True, null=True)
    http_status = models.CharField(verbose_name='http连接状态', max_length=30, blank=True, null=True)

# 异步消息接收
class AsynMsg(models.Model):
    notify_time = models.DateTimeField(verbose_name='通知时间', default=timezone.now())
    notify_type = models.CharField(verbose_name='通知类型', max_length=120)
    notify_id = models.CharField(verbose_name='通知校验ID', max_length=200)
    charset = models.CharField(verbose_name='编码格式', max_length=12)
    version = models.CharField(verbose_name='版本', max_length=8)
    sign_type = models.CharField(verbose_name='签名类型', max_length=12)
    sign = models.CharField(verbose_name='签名', max_length=249)
    auth_app_id = models.CharField(verbose_name='授权方的app_id', max_length=36)

# 业务参数
class ServiceParam(models.Model):
    trade_no = models.CharField(verbose_name='支付宝交易号', max_length=120)
    app_id = models.CharField(verbose_name='开发者的app_id', max_length=36)
    out_trade_no = models.CharField(verbose_name='商户订单号', max_length=80)
    out_biz_no = models.CharField(verbose_name='商户业务号', max_length=80)
    buyer_id = models.CharField(verbose_name='买家支付宝用户号', max_length=30)
    seller_id = models.CharField(verbose_name='卖家支付宝用户号', max_length=30)
    trade_status = models.CharField(verbose_name='交易状态', max_length=30)
    total_amount = models.DecimalField(verbose_name='订单金额', max_digits=10, decimal_places=2)
    receipt_amount = models.DecimalField(verbose_name='实收金额', max_digits=10, decimal_places=2)
    invoice_amount = models.DecimalField(verbose_name='开票金额', max_digits=10, decimal_places=2)
    buyer_pay_amount = models.DecimalField(verbose_name='付款金额', max_digits=10, decimal_places=2)
    point_amount = models.DecimalField(verbose_name='集分宝金额', max_digits=10, decimal_places=2)
    refund_fee = models.DecimalField(verbose_name='总退款金额', max_digits=10, decimal_places=2)
    subject = models.CharField(verbose_name='订单标题', max_length=200)
    body = models.CharField(verbose_name='商品描述', max_length=249)
    gmt_create = models.DateTimeField(verbose_name='交易创建时间', default=timezone.now())
    gmt_payment = models.DateTimeField(verbose_name='交易付款时间', default=timezone.now())
    gmt_refund = models.DateTimeField(verbose_name='交易退款时间', default=timezone.now())
    gmt_close = models.DateTimeField(verbose_name='交易结束时间', default=timezone.now())
    fund_bill_list = models.CharField(verbose_name='支付金额信息',max_length=240)
    voucher_detail_list = models.CharField(verbose_name='优惠券信息', max_length=240)
    passback_params = models.CharField(verbose_name='回传参数', max_length=240)

# 缓存数据
class CacheData(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    product_id = models.IntegerField(verbose_name='产品id')
    number = models.IntegerField(verbose_name='购买数量')
    cart_time = models.DateTimeField(verbose_name='购物车添加时间',default=timezone.now())

    class Meta:
        verbose_name = u"缓存数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.product_id)