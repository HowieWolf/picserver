from django import forms

from datamodel.models import CertRecord, User
from util.base.view import BaseView
from util.decorator.auth import cms_auth
from util.decorator.param import fetch_object, validate_args
from util.security import md5


class CertCheck(BaseView):

    @cms_auth
    @validate_args({
        'result': forms.BooleanField(),
    })
    @fetch_object(CertRecord.objects, 'cert')
    def post(self, request, cert, result, **kwargs):
        if cert.stage == CertRecord.STAGE_PASS or cert.stage == CertRecord.STAGE_REJECT:
            return self.fail(1, '无法重复审核')
        user = request.user
        if not result:
            CertRecord.objects.filter(id=cert.id).update(stage=CertRecord.STAGE_REJECT)
            User.objects.filter(id=user.id).update(stage_cert=CertRecord.STAGE_REJECT)
            return self.success()
        CertRecord.objects.filter(id=cert.id).update(stage=CertRecord.STAGE_PASS)
        User.objects.filter(id=user.id).update(
            stage_cert=CertRecord.STAGE_PASS, name=cert.name, appid=md5(user.username), secret=md5(user.password),
            qtoken=md5(user.token)
        )
        return self.success()
