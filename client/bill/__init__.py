from django.urls import path

from client.bill.list import PayBill, CancelBill

urlpatterns = [
    path('<int:bill_id>/pay/', PayBill.as_view()),
    path('<int:bill_id>/cancel/', CancelBill.as_view()),
]
