from datamodel.models import Copyright
from datamodel.models.config import ClientConfig

from similarity.dhash import DHash


def has_the_same_pic_with(origin):
    config = ClientConfig.objects.first()
    if not config or not config.enable_pic_similarity:
        return None
    # 当前图片的 dhash
    dhash = origin.dhash
    # 对比
    result = []
    qs = Copyright.qs.all()
    for p in qs:
        if DHash.hamming_distance(dhash, p.dhash) < config.threshold_for_hamming_in_pic_similarity:
            result.append(p)
    # 返回结果
    return result if len(result) > 0 else None
