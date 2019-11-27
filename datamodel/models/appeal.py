from django.db import models


class Appeal(models.Model):
    # 尚未提出申诉
    STATE_WAITING_APPEAL = 0
    # 提出申诉，等待审判者响应
    STATE_APPEALING = 1
    # 评审结束
    STATE_FINISH = 2

    # 申请人
    applicant = models.ForeignKey('User', related_name='appeals', on_delete=models.CASCADE)
    origin = models.OneToOneField('Copyright', related_name='+', on_delete=models.CASCADE)
    same = models.ManyToManyField('Copyright', related_name='+')
    state = models.IntegerField(default=STATE_WAITING_APPEAL)
    result = models.BooleanField(default=False)
    # 提出申请时间
    time_apply = models.DateTimeField(null=True)

    class Meta:
        db_table = 'appeal'


class AppealJudgement(models.Model):
    result = models.NullBooleanField(default=None)
    judge = models.ForeignKey('User', related_name='judgements', on_delete=models.CASCADE)
    appeal = models.ForeignKey('Appeal', related_name='suggestions', on_delete=models.CASCADE)
    # 审判者回应的时间
    time_judge = models.DateTimeField()

    class Meta:
        db_table = 'appeal_judgement'
