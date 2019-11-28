from django.db import models


class FinishCopyrightManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(state=True)


class Copyright(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, default='')
    author = models.ForeignKey('User', related_name='copyrights', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/copyright/%y/%m/%d')
    dhash = models.CharField(max_length=16, default='')
    # 价格，单位，分
    price = models.IntegerField(default=0)
    # 分类
    category = models.CharField(max_length=20, default='')
    # 是否版权通过
    state = models.BooleanField(default=True)
    # 版权通过的时间
    time_finish = models.DateTimeField()

    objects = models.Manager()
    qs = FinishCopyrightManager()

    class Meta:
        db_table = 'copyright'
        ordering = ['-time_finish']
