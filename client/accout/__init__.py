from django.urls import path

from client.accout.auth import RegisterAndLogin
from client.accout.money import Money

urlpatterns = [
    path('auth/', RegisterAndLogin.as_view()),
    path('money/', Money.as_view()),
]
