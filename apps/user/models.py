from django.db import models
import os

# 网站站点图片路径
WEB_IMG_DIR = os.path.join('','media','web_site')
# Create your models here.

# 用户登录帐号
class UserAccount(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=120, null=True)
    signature = models.CharField(verbose_name='个性签名', max_length=250, null=True, blank=True)
    user_acc = models.CharField(verbose_name='登录帐号', max_length=120)
    user_pwd = models.CharField(verbose_name='登录密码', max_length=250)
    phone = models.CharField(verbose_name='电话号码', max_length=120, unique=True, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱', max_length=250, unique=True, null=True, blank=True)
    log_time = models.DateTimeField(verbose_name='登录起始时间', auto_now_add=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

# 用户信息储存 一对一
class UserMessage(models.Model):
    realname = models.CharField(verbose_name='真实姓名', blank=True, max_length=120, null=True)
    face = models.ImageField(verbose_name='头像', blank=True, null=True, default=os.path.join(WEB_IMG_DIR,'default_face.png'))
    sex = models.CharField(verbose_name='性别',max_length=8, null=True)
    birth = models.DateField(verbose_name='生日', blank=True)
    sf_code = models.CharField(verbose_name='身份证号码', max_length=8, blank=True, null=True)
    is_member = models.NullBooleanField(verbose_name='是否是会员', default=None)
    user_account = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)

# 用户状态 一对一
class UserStatus(models.Model):
    is_18 = models.NullBooleanField(verbose_name='满18岁？', blank=True, null=True)
    is_marry = models.NullBooleanField(verbose_name='是否结婚', default=None)
    is_house = models.NullBooleanField(verbose_name='是否有房', default=None)
    is_car = models.NullBooleanField(verbose_name='是否有车', default=None)
    acc_status = models.CharField(verbose_name='帐号状态(num)', max_length=8, default='1')
    credit_status = models.CharField(verbose_name='信誉状况(分)', max_length=8, default='50')
    is_business = models.NullBooleanField(verbose_name='是否是商家', default=None)
    is_real = models.NullBooleanField(verbose_name='是否实名认证', default=None)
    user_account = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)

# 用户银行卡 一对多
class UserMoney(models.Model):
    card_num = models.CharField(verbose_name='银行卡号', max_length=120, null=True)
    card_status = models.CharField(verbose_name='信用卡状态(num)', max_length=8, default='1')
    card_useful_money = models.DecimalField(verbose_name='信用卡可用金额', max_digits=10, decimal_places=4)
    card_ice_money = models.DecimalField(verbose_name='信用卡冻结金额', max_digits=8, decimal_places=4)
    use_money_count = models.DecimalField(verbose_name='在网站消费了多少钱', max_digits=10, decimal_places=4)
    user_account = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
