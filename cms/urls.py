from django.urls import path, include

from cms import config

urlpatterns = [
    path('config/', include(config)),
]
