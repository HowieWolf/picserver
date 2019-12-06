from django.urls import path

from cms.cert.check import CertCheck
from cms.cert.list_detail import CertRecordList, CertRecordDetail

urlpatterns = [
    path('', CertRecordList.as_view()),
    path('<int:cert_id>/', CertRecordDetail.as_view()),
    path('<int:cert_id>/check/', CertCheck.as_view()),
]
