# Generated by Django 2.0.4 on 2018-04-23 05:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 23, 5, 50, 28, 695029, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='data_status',
            field=models.IntegerField(default=1, verbose_name='数据状态'),
        ),
    ]
