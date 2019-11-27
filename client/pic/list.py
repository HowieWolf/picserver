from django import forms

from datamodel.models import Copyright
from util.base.view import BaseView
from util.decorator.param import validate_args, fetch_object


class SearchByKeyword(BaseView):

    @validate_args({
        'category': forms.CharField(max_length=20, required=False),
        'key': forms.CharField(max_length=50),
    })
    def get(self, request, key, category=None, **kwargs):
        condition = {
            'name__icontains': key,
        }
        if category:
            condition['category'] = category
        qs = Copyright.qs.filter(**condition)
        return self.success([copyright_to_json(p) for p in qs])


class SearchHot(BaseView):
    def get(self, request, **kwargs):
        qs = Copyright.qs.all()
        return self.success([copyright_to_json(p) for p in qs])


class PicDetail(BaseView):
    @fetch_object(Copyright.objects, 'pic')
    def get(self, request, pic, **kwargs):
        return self.success(copyright_to_json(pic))


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
