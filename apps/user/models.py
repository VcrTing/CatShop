from django.db import models
from apps.web_config import *
#from apps.product.models import Product

# Create your models here.

# 用户登录帐号
class UserAccount(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=120, unique=True, null=True)
    phone = models.CharField(verbose_name='电话号码', max_length=120, unique=True, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱', max_length=250, unique=True, null=True, blank=True)
    user_pwd = models.CharField(verbose_name='登录密码', max_length=250)
    log_time = models.DateTimeField(verbose_name='登录起始时间', auto_now_add=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
        #(0、无， 1、可用， 2、具备支付能力， 3、用户指数极低 4、不可用)
    acc_status = models.IntegerField(verbose_name='帐号状态(num)', default=1)

    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"用户帐号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

# 用户信息储存 一对一
class UserMessage(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=120, unique=True, null=True)
    signature = models.CharField(verbose_name='个性签名', max_length=250, default=STR_DEFAULT, null=True, blank=True)
    realname = models.CharField(verbose_name='真实姓名', blank=True, max_length=120, null=True, default=STR_NUM_DEFAULT)
    face = models.ImageField(verbose_name='头像', upload_to="image/%Y/%m", blank=True, null=True, default=FACE_DEFAULT)
    sex = models.CharField(verbose_name='性别',max_length=8, null=True, default=STR_NUM_DEFAULT)
    birth = models.DateField(verbose_name='生日', blank=True, auto_now=True)
    sf_code = models.CharField(verbose_name='身份证号码', default=STR_NUM_DEFAULT, max_length=8, blank=True, null=True)
    is_member = models.NullBooleanField(verbose_name='是否是会员', default=BOOL_NULL_DEFAULT)
    #user_account = models.ForeignKey(UserAccount, verbose_name='所属用户', on_delete=models.SET_NULL, blank=True, null=True)
    user_account = models.OneToOneField(UserAccount, verbose_name='所属用户', on_delete=models.CASCADE, primary_key=True)
    user_id = models.IntegerField(verbose_name='用户id', null=True, blank=True)
    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname+'用户的资料'

# 用户状态 一对一
class UserStatus(models.Model):
    is_18 = models.NullBooleanField(verbose_name='满18岁？', default=BOOL_NULL_DEFAULT, blank=True, null=True)
    is_marry = models.NullBooleanField(verbose_name='是否结婚', default=BOOL_NULL_DEFAULT)
    is_house = models.NullBooleanField(verbose_name='是否有房', default=BOOL_NULL_DEFAULT)
    is_car = models.NullBooleanField(verbose_name='是否有车', default=BOOL_NULL_DEFAULT)
    credit_status = models.IntegerField(verbose_name='信誉状况(分)', default=INT_DEFAULT)
    is_business = models.NullBooleanField(verbose_name='是否是商家', default=BOOL_NULL_DEFAULT)
    is_real = models.NullBooleanField(verbose_name='是否实名认证', default=BOOL_NULL_DEFAULT)
    #user_account = models.ForeignKey(UserAccount, verbose_name='所属用户', on_delete=models.SET_NULL, blank=True, null=True)
    user_account = models.OneToOneField(UserAccount, verbose_name='所属用户', on_delete=models.CASCADE, primary_key=True)
    user_id = models.IntegerField(verbose_name='用户id', null=True, blank=True)
    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"用户状态详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户ID:'+str(self.user_id)+'的状态'

# 用户资金 一对一
class UserMoneyCount(models.Model):
    user_account = models.OneToOneField(UserAccount, verbose_name='所属用户', on_delete=models.CASCADE, primary_key=True)
    use_money_count = models.DecimalField(verbose_name='在网站消费了多少钱', default=DECIMAL_DEFAULT_ZERO, max_digits=10, decimal_places=2)
    product_num = models.IntegerField(verbose_name='已买多少件商品', null=True)
    email = models.EmailField(verbose_name='保存的邮箱', max_length=250, unique=True, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    data_status = models.IntegerField(verbose_name='数据状态', default=1)
    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"用户消费记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.email)+'的消费记录'
