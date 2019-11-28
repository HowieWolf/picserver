from django.db import models


class ClientConfig(models.Model):
    enable_pic_similarity = models.BooleanField(default=True)
    threshold_for_hamming_in_pic_similarity = models.IntegerField(default=10)

    class Meta:
        db_table = 'config_client'
