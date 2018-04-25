# Generated by Django 2.0.4 on 2018-04-23 04:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asynmsg',
            name='notify_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 4, 11, 25, 791253, tzinfo=utc), verbose_name='通知时间'),
        ),
        migrations.AlterField(
            model_name='cachedata',
            name='cart_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 4, 11, 25, 792621, tzinfo=utc), verbose_name='购物车添加时间'),
        ),
        migrations.AlterField(
            model_name='serviceparam',
            name='gmt_close',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 4, 11, 25, 792026, tzinfo=utc), verbose_name='交易结束时间'),
        ),
        migrations.AlterField(
            model_name='serviceparam',
            name='gmt_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 4, 11, 25, 791965, tzinfo=utc), verbose_name='交易创建时间'),
        ),
        migrations.AlterField(
            model_name='serviceparam',
            name='gmt_payment',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 4, 11, 25, 791990, tzinfo=utc), verbose_name='交易付款时间'),
        ),
        migrations.AlterField(
            model_name='serviceparam',
            name='gmt_refund',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 4, 11, 25, 792008, tzinfo=utc), verbose_name='交易退款时间'),
        ),
    ]
