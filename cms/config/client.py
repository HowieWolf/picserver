from django import forms

from datamodel.models.config import ClientConfig
from util.base.view import BaseView
from util.decorator.param import validate_args


class ManageClientConfig(BaseView):
    def get(self, request, **kwargs):
        c = ClientConfig.objects.first()
        if c is None:
            return self.fail(1, '尚未配置项')
        return self.success({
            'enable_pic_similarity': c.enable_pic_similarity,
            'threshold_for_hamming_in_pic_similarity': c.threshold_for_hamming_in_pic_similarity,
        })

    @validate_args({
        'enable_pic_similarity': forms.BooleanField(required=False),
        'threshold_for_hamming_in_pic_similarity': forms.IntegerField(required=False),
    })
    def post(self, request, **kwargs):
        config_list = ['enable_pic_similarity', 'threshold_for_hamming_in_pic_similarity']
        data = {}
        for k in config_list:
            if k in kwargs:
                data[k] = kwargs.get(k)
        if ClientConfig.objects.exists():
            ClientConfig.objects.all().update(**data)
        else:
            ClientConfig.objects.create(**data)
        return self.success()
