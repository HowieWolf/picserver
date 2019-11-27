from datetime import datetime

from django import forms

from datamodel.models import Appeal, AppealJudgement, Copyright
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import validate_args, fetch_object


class JudgeAppeal(BaseView):

    @client_auth
    @validate_args({
        'result': forms.BooleanField(),
    })
    @fetch_object(Appeal.objects, 'appeal')
    def post(self, request, appeal, result, **kwargs):
        if appeal.state != Appeal.STATE_APPEALING:
            return self.fail(1, '当前阶段无法评审')
        judgement = AppealJudgement.objects.filter(judge=request.user, appeal=appeal).first()
        if judgement is None:
            return self.fail(2, '您未参与评审')
        if judgement.result is not None:
            return self.fail(3, '您已评审完毕')
        now = datetime.now()
        AppealJudgement.objects.filter(id=judgement.id).update(result=result, time_judge=now)
        count = appeal.suggestions.all().count()
        count_judge = appeal.suggestions.exclude(result=None).count()
        # 仍有评审者未评审
        if count_judge < count:
            return self.success()
        # 统计结果
        count_right = appeal.suggestions.filter(result=True).count()
        result = count_right / count > 0.8
        Appeal.objects.filter(id=appeal.id).update(state=Appeal.STATE_FINISH, result=result)
        Copyright.objects.filter(id=appeal.origin.id).update(state=result, time_finish=now)
        return self.success()
