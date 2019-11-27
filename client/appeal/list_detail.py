from django import forms

from datamodel.models import Appeal
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import validate_args, fetch_object


class MyAppealList(BaseView):

    @client_auth
    @validate_args({
        'state': forms.IntegerField(required=False),
    })
    def get(self, request, state=None, **kwargs):
        if state is not None and state not in Appeal.STATES_NORMAL:
            return self.fail(1, '状态不正确')
        condition = {
            'applicant': request.user,
        }
        if state:
            condition['state'] = state
        qs = Appeal.qs.filter(**condition)
        return self.success([appeal_to_json(a) for a in qs])


class MyJudgeAppealList(BaseView):

    @client_auth
    @validate_args({
        'state': forms.IntegerField(required=False),
    })
    def get(self, request, state=None, **kwargs):
        if state is not None and state not in Appeal.STATES_NORMAL:
            return self.fail(1, '状态不正确')
        condition = {
            'suggestions__judge': request.user,
        }
        if state:
            condition['state'] = state
        qs = Appeal.qs.filter(**condition)
        return self.success([appeal_to_json(a) for a in qs])


class AppealDetail(BaseView):
    @client_auth
    @fetch_object(Appeal.qs, 'appeal')
    def get(self, request, appeal, **kwargs):
        info = {
            'same': [pic_to_json(p) for p in appeal.same.all()],
        }
        judge = appeal.suggestions.filter(judge=request.user).first()
        info['need_judge'] = judge is not None
        if judge:
            info['result'] = judge.result
        return self.success(appeal_to_json(appeal, **info))


def appeal_to_json(a, **kwargs):
    return {
        'id': a.id,
        'time_apply': a.time_apply,
        'state': a.state,
        'origin': pic_to_json(a.origin),
        **kwargs
    }


def pic_to_json(p):
    return {
        'id': p.id,
        'url': p.img.url,
        'name': p.name,
        'category': p.category,
    }
