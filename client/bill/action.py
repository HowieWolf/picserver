from datetime import datetime

from datamodel.models import User
from datamodel.models.bill import Bill
from util.base.view import BaseView
from util.decorator.auth import client_auth
from util.decorator.param import fetch_object


class PayBill(BaseView):

    @client_auth
    @fetch_object(Bill.objects, 'bill')
    def post(self, request, bill, **kwargs):
        if bill.state != Bill.STATE_PAYING:
            return self.fail(2, '当前无法支付')
        user = request.user
        if user.money < bill.cost:
            return self.fail(1, '余额不足')
        User.objects.filter(id=user.id).update(money=user.money - bill.cost)
        Bill.objects.filter(id=bill.id).update(state=Bill.STATE_FINISH, time_pay=datetime.now())
        return self.success()


class CancelBill(BaseView):
    @client_auth
    @fetch_object(Bill.objects, 'bill')
    def delete(self, request, bill, **kwargs):
        if bill.state == Bill.STATE_FINISH:
            return self.fail(2, '订单已完成，无法取消')
        Bill.objects.filter(id=bill.id).update(state=Bill.STATE_CANCEL)
        return self.success()
