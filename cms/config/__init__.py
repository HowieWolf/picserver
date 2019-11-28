from django.urls import path

from cms.config.client import ManageClientConfig

urlpatterns = [
    path('client/', ManageClientConfig.as_view()),
]
