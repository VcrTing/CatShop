# Generated by Django 2.0.4 on 2018-04-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMoneyRecord',
            new_name='UserMoneyCount',
        ),
    ]