from django.urls import path, include
from cms import copyright, config, control, adminuser, account, cert

urlpatterns = [
    path('copyright/', include(copyright)),
    path('config/', include(config)),
    path('', include(control)),
    path('adminuser/', include(adminuser)),
    path('account/', include(account)),
    path('cert/', include(cert)),
]
