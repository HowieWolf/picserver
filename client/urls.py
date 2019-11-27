from django.urls import path, include

from client import accout, copyright

urlpatterns = [
    path('account/', include(accout)),
    path('copyright/', include(copyright)),
]
