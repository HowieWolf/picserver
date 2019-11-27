from django.urls import path, include

from client import accout, copyright, appeal, pic, bill

urlpatterns = [
    path('account/', include(accout)),
    path('copyright/', include(copyright)),
    path('appeal/', include(appeal)),
    path('pic/', include(pic)),
    path('bill/', include(bill)),
]
