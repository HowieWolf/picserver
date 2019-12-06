from django.urls import path

from client.accout.auth import RegisterAndLogin
from client.accout.cert import MyCert
from client.accout.info import Info
from client.accout.money import Money

urlpatterns = [
    path('auth/', RegisterAndLogin.as_view()),
    path('money/', Money.as_view()),
    path('info/', Info.as_view()),
    path('cert/', MyCert.as_view()),
]
