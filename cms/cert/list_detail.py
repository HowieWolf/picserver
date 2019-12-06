from django import forms

from datamodel.models import CertRecord
from util.base.view import BaseView
from util.decorator.auth import cms_auth
from util.decorator.param import validate_args, fetch_object


class CertRecordList(BaseView):

    @cms_auth
    @validate_args({
        'stage': forms.IntegerField(required=False),
    })
    def get(self, request, stage=None, **kwargs):
        filter = {}
        if stage:
            filter['stage'] = stage
        qs = CertRecord.objects.filter(**filter)
        return self.success_list(request, qs, cert_to_josn)


class CertRecordDetail(BaseView):
    @cms_auth
    @fetch_object(CertRecord.objects, 'cert')
    def get(self, request, cert, **kwargs):
        return self.success(cert_to_josn(cert))


def cert_to_josn(cert):
    return {
        'id': cert.id,
        'name': cert.name,
        'pic': cert.certificate.url,
        'stage': cert.stage,
    }
