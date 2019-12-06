from django.urls import re_path

from cms.adminuser.control import ResetPassword, EnableControl
from cms.adminuser.list_detail import AllAdminUserList, ManagerControlledByMe, AdminUserDetail

urlpatterns = [
    # 筛选管理端用户
    re_path(r'^$', AllAdminUserList.as_view()),
    re_path(r'^my/$', ManagerControlledByMe.as_view()),
    # 用户详情
    re_path(r'^(?P<user_id>\d+)/$', AdminUserDetail.as_view()),
    re_path(r'^(?P<user_id>\d+)/resetpsd/$', ResetPassword.as_view()),
    re_path(r'^(?P<user_id>\d+)/enable/$', EnableControl.as_view()),
]
