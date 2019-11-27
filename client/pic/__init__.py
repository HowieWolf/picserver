from django.urls import path

from client.pic.list import SearchByKeyword, SearchHot
from client.pic.buy import PicDetail, BuyPic

urlpatterns = [
    path('search/', SearchByKeyword.as_view()),
    path('hot/', SearchHot.as_view()),
    path('<int:pic_id>/', PicDetail.as_view()),
    path('<int:pic_id>/buy/', BuyPic.as_view()),
]
