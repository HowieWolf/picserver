from django.db import models


class Bill(models.Model):
    STATE_PAYING = 0
    STATE_FINISH = 1
    STATE_CANCEL = 2

    STATES_ALL = [STATE_PAYING, STATE_FINISH, STATE_CANCEL, ]

    pic = models.ForeignKey('Copyright', related_name='bills', on_delete=models.CASCADE)
    # 支付金额
    cost = models.IntegerField()
    user = models.ForeignKey('User', related_name='bills', on_delete=models.CASCADE)
    state = models.IntegerField(default=STATE_PAYING)
    time_create = models.DateTimeField(auto_now_add=True)
    time_pay = models.DateTimeField(null=True)

    class Meta:
        db_table = 'bill_pic'
        ordering = ['-time_create']
