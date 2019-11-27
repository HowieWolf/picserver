from datetime import datetime

from django import forms

from datamodel.models import Copyright, Appeal
from similarity import has_the_same_pic_with
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import validate_args, fetch_object


class CopyrightList(BaseView):

    def get(self, request, **kwargs):
        return self.fail(2)
        pass

    @client_auth
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
        # 对比相似度
        result = has_the_same_pic_with(right)
        if result is None:
            return self.success({
                'id': right.id
            })
        # 依据相似度结果，判断是否创建申诉
        Copyright.objects.filter(id=right.id).update(state=False)
        appeal = Appeal.objects.create(applicant=request.user, origin=right)
        for p in result:
            appeal.same.add(p)
        return self.fail(1, data={
            'id': appeal.id,
            'pics': [copyright_to_json(p) for p in result]
        })


class CopyrightDetail(BaseView):
    @fetch_object(Copyright.qs, 'copyright')
    def get(self, request, copyright, **kwargs):
        return self.success(copyright_to_json(copyright))


def copyright_to_json(p):
    return {
        'id': p.id,
        'name': p.name,
        'desc': p.desc,
        'url': p.img.url,
        'category': p.category,
        'author_name': p.author.name,
        'author_id': p.author.id,
        'price': p.price,
        'time': p.time_finish,
    }
