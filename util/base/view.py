from django.http import JsonResponse
from django.views import View


class BaseView(View):

    def success(self, data=None):
        return JsonResponse({
            'code': 0,
            'data': data
        })

    def fail(self, code, msg='', **kwargs):
        return JsonResponse({
            'code': code,
            'msg': msg,
            **kwargs
        })
