from django.urls import path

from client.pic.list import SearchByKeyword, SearchHot, PicDetail

urlpatterns = [
    path('search/', SearchByKeyword.as_view()),
    path('hot/', SearchHot.as_view()),
    path('<int:pic_id>/', PicDetail.as_view()),
]
