from django import forms
from django.http import JsonResponse
from django.views import View

from util.decorator.param import validate_args


class BaseView(View):

    def success(self, data=None):
        return JsonResponse({
            'code': 0,
            'data': data
        })

    @validate_args({
        'page': forms.IntegerField(min_value=0, required=False),
        'limit': forms.IntegerField(min_value=1, required=False),
    })
    def success_list(self, request, iter, obj_to_json, page=0, limit=10):
        return self.success({
            'totalCount': len(iter),
            'list': [obj_to_json(o) for o in iter[page * limit:(page + 1) * limit]]
        })

    def fail(self, code, msg='', **kwargs):
        return JsonResponse({
            'code': code,
            'msg': msg,
            **kwargs
        })
