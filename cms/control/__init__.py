from django.urls import re_path

from cms.control.function import AllFunctionList, MyFunctionList, FunctionDetail
from cms.control.role import AllRoleList, MyRoleDetail, RoleControlledByMe, RoleDetail
from cms.control.role_function import RoleFunction, ManageRoleFunction
from cms.control.user_role import ManageUserRole

urlpatterns = [
    # 所有角色列表
    re_path(r'^role/$', AllRoleList.as_view()),
    # 我的角色详情
    re_path(r'^role/my/$', MyRoleDetail.as_view()),
    # 我管理的角色列表
    re_path(r'^role/child/$', RoleControlledByMe.as_view()),
    # 角色详情
    re_path(r'^role/(?P<role_id>\d+)/$', RoleDetail.as_view()),
    # 角色拥有的功能
    re_path(r'^role/(?P<role_id>\d+)/function/$', RoleFunction.as_view()),
    # 管理角色的功能
    re_path(r'^role/(?P<role_id>\d+)/function/(?P<function_id>\w+)/$', ManageRoleFunction.as_view()),
    # 所有功能列表
    re_path(r'^function/$', AllFunctionList.as_view()),
    # 我的功能列表
    re_path(r'^function/my/$', MyFunctionList.as_view()),
    # 功能详情
    re_path(r'^function/(?P<function_id>\w+)/$', FunctionDetail.as_view()),
    # 为用户指派角色
    re_path(r'^permission/user/(?P<user_id>\w+)/$', ManageUserRole.as_view())
]
