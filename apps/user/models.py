from django.db import models

# Create your models here.
class UserAccount(models.Model):
    user_acc = models.CharField(max_length=120)
    user_pwd = models.CharField(max_length=300)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=300, unique=True)

class UserMessage(models.Model):
    realname = models.CharField(max_length=120)
    face = models.ImageField()