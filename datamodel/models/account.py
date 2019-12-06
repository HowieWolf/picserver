from django.db import models

# Create your models here.
from datamodel.models.cert import CertRecord


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=256)
    # 账户余额
    money = models.IntegerField(default=0)

    stage_cert = models.IntegerField(default=CertRecord.STAGE_NO)
    appid = models.CharField(max_length=32, null=True, default=None)
    secret = models.CharField(max_length=64, null=True, default=None)
    qtoken = models.CharField(max_length=256, null=True, default=None)

    class Meta:
        db_table = 'user'


class AdminUser(models.Model):
    """超级管理员"""

    is_enabled = models.BooleanField(default=True, db_index=True)
    username = models.CharField(max_length=20, unique=True, db_index=True)
    password = models.CharField(max_length=128)
    # 系统角色
    system_role = models.ForeignKey('CMSRole', related_name='users', default=None, null=True, on_delete=models.CASCADE)
    # token
    token = models.CharField(max_length=254, default='')

    name = models.CharField(max_length=15, default='', db_index=True)

    objects = models.Manager()

    class Meta:
        db_table = 'admin_user'
