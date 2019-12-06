from django.db import models


class CertRecord(models.Model):
    # 未申请
    STAGE_NO = 0
    # 等待审核
    STAGE_APPLY = 1
    # 通过
    STAGE_PASS = 2
    # 拒绝
    STAGE_REJECT = 3

    user = models.ForeignKey('User', related_name='cert_records', on_delete=models.CASCADE)
    stage = models.IntegerField(default=STAGE_APPLY)
    name = models.CharField(max_length=30, default='')
    certificate = models.ImageField(upload_to='static/certificate/%y/%m/%d')

    class Meta:
        db_table = 'cert_record'
        ordering = ['-id']
