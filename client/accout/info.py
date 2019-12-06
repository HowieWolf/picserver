from datamodel.models import CertRecord
from util.base.view import BaseView
from util.decorator.auth import client_auth


class Info(BaseView):
    @client_auth
    def get(self, request):
        return self.success({
            'name': request.user.name,
            'money': request.user.money,
            'type': 1 if request.user.stage_cert == CertRecord.STAGE_PASS else 0
        })
