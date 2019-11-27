from django import forms

from datamodel.models import User
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import validate_args


class Money(BaseView):
    @client_auth
    def get(self, request):
        return self.success({
            'name': request.user.name,
            'money': request.user.money,
        })

    @client_auth
    @validate_args({
        'money': forms.IntegerField(min_value=1),
    })
    def post(self, request, money, **kwargs):
        user = request.user
        User.objects.filter(id=user.id).update(money=user.money + money)
        return self.success()
