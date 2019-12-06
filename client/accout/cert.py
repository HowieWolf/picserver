from django import forms

from datamodel.models import User, CertRecord
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import validate_args


class MyCert(BaseView):

    @client_auth
    def get(self, request, **kwargs):
        user = request.user
        stage = user.stage_cert
        result = {
            'stage': stage
        }
        if stage == CertRecord.STAGE_PASS:
            result['appid'] = user.appid
            result['secret'] = user.secret
            result['name'] = user.name
        return self.success(result)

    @client_auth
    @validate_args({
        'name': forms.CharField(max_length=30, min_length=1),
        'pic': forms.ImageField(),
    })
    def post(self, request, name, pic, **kwargs):
        user = request.user
        if user.stage_cert == CertRecord.STAGE_PASS:
            return self.fail(1, '已经认证通过，无需重复认证')
        if user.stage_cert == CertRecord.STAGE_APPLY:
            return self.fail(2, '认证审核中，请稍后')
        CertRecord.objects.create(name=name, certificate=pic, user=user)
        User.objects.filter(id=user.id).update(stage_cert=CertRecord.STAGE_APPLY)
        return self.success()
