from django.urls import path

from cms.copyright.clear import ClearErrorCopyright
from cms.copyright.fill_dhash import FillDHashForCopyright

urlpatterns = [
    path('fill/', FillDHashForCopyright.as_view()),
    path('clearerror/', ClearErrorCopyright.as_view()),
]
