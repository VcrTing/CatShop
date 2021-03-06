# Generated by Django 2.0.4 on 2018-04-23 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20180423_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 11, 34, 57, 577341, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('default', '初始状态'), ('confirm', '货物派发中'), ('waitReview', '等待评价'), ('finish', '交易完成')], default='default', max_length=20, verbose_name='订单项状态'),
        ),
    ]
