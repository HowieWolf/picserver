from datetime import datetime

from django import forms

from datamodel.models.contract import EContract
from util.base.view import BaseView
from util.decorator.auth import cms_auth
from util.decorator.param import validate_args, fetch_object
from util.decorator.permission import cms_permission


class UploadedContractList(BaseView):

    @cms_auth
    @validate_args({
        'stage': forms.IntegerField(required=False),
    })
    def get(self, request, stage=None, **kwargs):
        filter = {}
        if stage:
            filter['stage'] = stage
        qs = EContract.objects.filter(**filter)
        return self.success_list(request, qs, contract_to_json)

    @cms_auth
    @cms_permission('uploadContract')
    @validate_args({
        'desc': forms.CharField(max_length=256),
        'file': forms.FileField(),
    })
    def post(self, request, desc, file, **kwargs):
        EContract.objects.create(desc=desc, file=file)
        return self.success()


class DeployContract(BaseView):
    @cms_auth
    @cms_permission('deployContract')
    @fetch_object(EContract.objects, 'contract')
    def post(self, request, contract, **kwargs):
        if contract.stage == EContract.STAGE_DEPLOY:
            return self.fail(1, '已部署的智能合约无法重复部署')
        # TODO 部署智能合约

        # 更新啊状态
        EContract.objects.filter(id=contract.id).update(
            stage=EContract.STAGE_DEPLOY, time_deploy=datetime.now(), address='')
        return self.success()


class UploadedContractAction(BaseView):
    @cms_auth
    @cms_permission('deleteContract')
    @fetch_object(EContract.objects, 'contract')
    def delete(self, request, contract, **kwargs):
        if contract.stage == EContract.STAGE_DEPLOY:
            return self.fail(1, '已部署的智能合约不能删除')
        contract.delete()
        return self.success()


def contract_to_json(c):
    return {
        'id': c.id,
        'desc': c.desc,
        'stage': c.stage,
    }
