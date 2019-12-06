from django.urls import path, include
from cms import copyright, config, control, adminuser, account, cert, contract

urlpatterns = [
    path('copyright/', include(copyright)),
    path('config/', include(config)),
    # 权限
    path('', include(control)),
    path('adminuser/', include(adminuser)),
    path('account/', include(account)),
    path('cert/', include(cert)),
    path('contract/', include(contract)),
]
