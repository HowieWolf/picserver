from django.urls import path

from client.copyright.appeal import CopyrightAppeal
from client.copyright.apply_detail import CopyrightList, CopyrightDetail
from client.copyright.list import MyCreateCopyright, MyPayCopyright

urlpatterns = [
    path('', CopyrightList.as_view()),
    path('create/', MyCreateCopyright.as_view()),
    path('buy/', MyPayCopyright.as_view()),
    path('<int:copyright_id>/', CopyrightDetail.as_view()),
    path('appeal/<int:appeal_id>/', CopyrightAppeal.as_view()),
]
