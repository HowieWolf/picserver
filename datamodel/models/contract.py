from django.db import models


class EContract(models.Model):
    STAGE_UPLOAD = 0
    STAGE_DEPLOY = 1

    desc = models.CharField(max_length=256, default='')
    file = models.FileField(upload_to='static/contract/%y/%m/%d')
    stage = models.IntegerField(default=STAGE_UPLOAD)
    # 部署后的合约地址
    address = models.CharField(max_length=40, null=True, default=None)
    time_deploy = models.DateTimeField(default=None, null=True)

    class Meta:
        db_table = 'ethereum_contract'
        ordering = ['-id']
