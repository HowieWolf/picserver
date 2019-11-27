from datamodel.models import Copyright
from datamodel.models.bill import Bill
from util.base.view import BaseView
from util.decorator.auth import client_auth


class MyCreateCopyright(BaseView):

    @client_auth
    def get(self, request):
        qs = Copyright.qs.filter(author=request.user, state=True)
        return self.success([copyright_to_json(p) for p in qs])


class MyPayCopyright(BaseView):
    @client_auth
    def get(self, request):
        qs = Copyright.qs.filter(bills__user=request.user, bills__state=Bill.STATE_FINISH)
        return self.success([copyright_to_json(p) for p in qs])


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
