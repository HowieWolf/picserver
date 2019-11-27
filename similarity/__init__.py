import random

from datamodel.models import Copyright


def has_the_same_pic_with(origin):
    if random.random() < 0.5:
        return None
    return Copyright.qs.all()[0:3]
    # 计算当前图片的指纹
    # 对比
    # 返回结果
    pass
