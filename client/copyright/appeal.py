from datetime import datetime

from datamodel.models import Appeal, User, AppealJudgement
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import fetch_object


class CopyrightAppeal(BaseView):

    @client_auth
    @fetch_object(Appeal.objects, 'appeal')
    def post(self, request, appeal, **kwargs):
        if appeal.applicant != request.user:
            return self.fail(4, '无权申诉')
        if appeal.origin.state:
            return self.fail(1, '当前版权已审核通过，无需申诉')
        if appeal.state == Appeal.STATE_FINISH:
            return self.fail(2, '申诉已完成，不能再次申诉')
        if appeal.state == Appeal.STATE_APPEALING:
            return self.fail(3, '申诉评审中，请等待')
        Appeal.objects.filter(id=appeal.id).update(state=Appeal.STATE_APPEALING, time_apply=datetime.now())
        # 筛选出评判者
        for p in User.objects.exclude(id=request.user.id).all()[0:10]:
            AppealJudgement.objects.create(judge=p, appeal=appeal)
        return self.success()
