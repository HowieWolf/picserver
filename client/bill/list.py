from datamodel.models.bill import Bill
from util.base.view import BaseView
from util.decorator.auth import client_auth


class MyPayBillList(BaseView):

    @client_auth
    def get(self, request):
        qs = Bill.objects.filter(user=request.user)
        return self.success([bill_to_json(b) for b in qs])


class PayToMeBillList(BaseView):

    @client_auth
    def get(self, request):
        qs = Bill.objects.filter(pic__author=request.user)
        return self.success([bill_to_json(b) for b in qs])


def bill_to_json(b):
    return {
        'id': b.id,
        'cost': b.cost,
        'state': b.state,
        'time_create': b.time_create,
        'time_pay': b.time_pay,
        'pic': {
            'id': b.pic.id,
            'url': b.pic.img.url,
            'name': b.pic.name,
            'category': b.pic.category,
        }
    }
