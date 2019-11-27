from datamodel.models import Copyright
from datamodel.models.bill import Bill
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import fetch_object


class PicDetail(BaseView):
    @fetch_object(Copyright.objects, 'pic')
    def get(self, request, pic, **kwargs):
        return self.success(copyright_to_json(pic))


class BuyPic(BaseView):

    @client_auth
    @fetch_object(Copyright.objects, 'pic')
    def post(self, request, pic, **kwargs):
        user = request.user
        if pic.author == user:
            return self.fail(1, '你是版权拥有者，无需购买')
        if Bill.objects.filter(pic=pic, user=user).exists():
            return self.fail(2, '你已经购买，无需重复购买')
        bill = Bill.objects.create(pic=pic, cost=pic.price, user=user)
        return self.success({
            'id': bill.id,
        })


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
