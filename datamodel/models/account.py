from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=256)
    # 账户余额
    money = models.IntegerField(default=0)

    class Meta:
        db_table = 'user'
