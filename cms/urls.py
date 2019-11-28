from django.urls import path, include
from cms import copyright, config

urlpatterns = [
    path('copyright/', include(copyright)),
    path('config/', include(config)),
]
