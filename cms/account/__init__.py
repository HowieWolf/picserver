from django.urls import re_path

from cms.account.auth import LoginByUsername
from cms.account.info import UserInfo

urlpatterns = [
    # 登录
    re_path(r'^auth/username/$', LoginByUsername.as_view()),
    # 用户详情
    re_path(r'^info/$', UserInfo.as_view()),
]
