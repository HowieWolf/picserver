from django.urls import path, include

from client import accout

urlpatterns = [
    path('account/', include(accout)),
]
