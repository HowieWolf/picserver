from django.urls import path

from client.bill.action import PayBill, CancelBill
from client.bill.list import MyPayBillList, PayToMeBillList

urlpatterns = [
    path('pay/', MyPayBillList.as_view()),
    path('gain/', PayToMeBillList.as_view()),
    path('<int:bill_id>/pay/', PayBill.as_view()),
    path('<int:bill_id>/cancel/', CancelBill.as_view()),
]
