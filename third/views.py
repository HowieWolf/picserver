import os
from datetime import datetime

from PIL import Image
from django import forms

# Create your views here.
from datamodel.models import User, CertRecord, Copyright
from picserver.settings import BASE_DIR
from similarity import DHash, has_the_same_pic_with
from util.base.view import BaseView
from util.decorator.auth import third_auth
from util.decorator.param import validate_args


class GetToken(BaseView):

    @validate_args({
        'appid': forms.CharField(max_length=32),
        'secret': forms.CharField(max_length=64),
    })
    def get(self, request, appid, secret, **kwargs):
        user = User.objects.filter(appid=appid, secret=secret, stage_cert=CertRecord.STAGE_PASS).first()
        if user is None:
            return self.fail(1, '请企业认证')
        return self.success({
            'access_token': user.qtoken,
        })


class RegisterCopyright(BaseView):

    @third_auth
    @validate_args({
        'name': forms.CharField(max_length=50),
        'desc': forms.CharField(max_length=200, required=False),
        'price': forms.IntegerField(min_value=0),
        'category': forms.CharField(max_length=20),
        'pic': forms.ImageField(),
    })
    def post(self, request, name, price, category, pic, desc='', **kwargs):
        user = request.user
        # 重命名
        now = datetime.now()
        pic.name = str(user.id) + now.strftime('%H%M%S') + pic.name
        # 创建 Copyright
        right = Copyright.objects.create(name=name, desc=desc, author=user, img=pic, price=price,
                                         category=category, time_finish=now)
        # 计算 dhash
        dhash = DHash.calculate_hash(Image.open(os.path.join(BASE_DIR, right.img.url)))
        Copyright.objects.filter(id=right.id).update(dhash=dhash)
        # 对比相似度
        result = has_the_same_pic_with(right, dhash)
        if result is None:
            return self.success({
                'id': right.id
            })
        return self.fail(1, '版权已存在')
