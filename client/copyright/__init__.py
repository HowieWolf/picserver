from django.urls import path, re_path

from client.copyright.apply_detail import CopyrightList, CopyrightDetail

urlpatterns = [
    path('', CopyrightList.as_view()),
    path('<int:copyright_id>/', CopyrightDetail.as_view()),
]
