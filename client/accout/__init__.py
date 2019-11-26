from django.urls import path

from client.accout.auth import RegisterAndLogin

urlpatterns = [
    path('auth/', RegisterAndLogin.as_view()),
]
