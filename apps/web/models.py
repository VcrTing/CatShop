from django.db import models
import datetime

# Create your models here.
class WebMessage(models.Model):
    register_num = models.CharField(verbose_name='注册人数', max_length=200, default='猫之商城')
    oline_num = models.CharField(verbose_name='在线人数', max_length=200, default='猫之商城')
    site_running_time = models.DateTimeField(verbose_name='站点开始运行的时间', auto_now_add=True)
    site_front_status = models.NullBooleanField(verbose_name='前台站点开启状态', default=True)
    site_message = models.CharField(verbose_name='站点全局信息', max_length=250, default='无')