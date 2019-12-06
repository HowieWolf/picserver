from django.urls import path

from third.views import GetToken, RegisterCopyright

urlpatterns = [
    path('getAccessToken/', GetToken.as_view()),
    path('registerCopyright/', RegisterCopyright.as_view()),
]
