from django import forms

from datamodel.models.account import User
from util.auth import generate_token
from util.base.view import BaseView
from util.decorator.param import validate_args


class RegisterAndLogin(BaseView):

    @validate_args({
        'username': forms.CharField(max_length=50),
        'psd': forms.CharField(max_length=32, min_length=6),
    })
    def get(self, request, username, psd, **kwargs):
        if not User.objects.filter(username=username).exists():
            return self.fail(1, '用户不存在')
        u = User.objects.filter(username=username, password=psd).first()
        if u is None:
            return self.fail(2, '密码错误')
        return self.success({
            'token': u.token
        })

    @validate_args({
        'username': forms.CharField(max_length=50),
        'psd': forms.CharField(max_length=32, min_length=6),
        'name': forms.CharField(max_length=50),
    })
    def post(self, request, username, psd, name, **kwargs):
        if User.objects.filter(username=username).exists():
            return self.fail(1, '用户名已存在')
        User.objects.create(username=username, password=psd, name=name, token=generate_token(username))
        return self.success()
