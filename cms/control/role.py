from django import forms

from cms.util.decorator.permission import cms_permission_role
from cms.util.role import role_to_json, get_all_child_role, compare_role
from datamodel.models import CMSRole
from util.base.view import BaseView
from util.code.error import NO_PERMISSION
from util.decorator.auth import cms_auth
from util.decorator.param import validate_args, fetch_object
from util.decorator.permission import cms_permission


class AllRoleList(BaseView):
    '''
    所有角色列表和创建角色，都需要权限
    '''

    @cms_auth
    @cms_permission('allRoleList')
    @validate_args({
        'category': forms.CharField(max_length=100, required=False),
    })
    def get(self, request, category=None,  **kwargs):
        filter_param = {}
        if category is not None:
            filter_param['category'] = category
        qs = CMSRole.objects.filter(**filter_param)
        return self.success_list(request, qs, role_to_json)

    @cms_auth
    @cms_permission('createRole')
    @validate_args({
        'name': forms.CharField(max_length=100),
        'category': forms.CharField(max_length=100, required=False),
        'enable': forms.NullBooleanField(required=False),
        'parent_role_id': forms.IntegerField(required=False),
    })
    @fetch_object(CMSRole.objects, 'parent_role', force=False)
    def post(self, request, name, parent_role=None, category='', enable=False, **kwargs):
        my_role = request.user.system_role
        # 如果指定的角色，不是我管理的角色，则没有权限
        if parent_role and parent_role != my_role and not compare_role(my_role, parent_role):
            return self.fail(NO_PERMISSION)
        # 未指定父角色，以我的角色作为父角色
        if parent_role is None:
            parent_role = my_role
        CMSRole.objects.create(name=name, category=category, enable=enable,
                               level=parent_role.level + 1,
                               parent_role=parent_role)
        return self.success()


class RoleControlledByMe(BaseView):
    '''我管理的角色，不需要权限'''

    @cms_auth
    @validate_args({
        'page': forms.IntegerField(required=False),
        'limit': forms.IntegerField(required=False),
        'category': forms.CharField(max_length=100, required=False),
    })
    def get(self, request,  **kwargs):
        # 获取我的角色列表
        my_role = request.user.system_role
        filter_param = {}
        if 'category' in kwargs:
            filter_param['category'] = kwargs['category']
        roles = get_all_child_role(my_role, **filter_param)
        return self.success_list(request, roles, role_to_json)


class MyRoleDetail(BaseView):

    @cms_auth
    def get(self, request, **kwargs):
        return self.success(role_to_json(request.user.system_role))


class RoleDetail(BaseView):

    @cms_auth
    @validate_args({
        'role_id': forms.IntegerField(),
    })
    @fetch_object(CMSRole.objects, 'role')
    @cms_permission_role()
    def get(self, request, role, **kwargs):
        return self.success(role_to_json(role))

    @cms_auth
    @cms_permission('updateRoleInfo')
    @validate_args({
        'role_id': forms.IntegerField(),
        'name': forms.CharField(max_length=100, required=False),
        'category': forms.CharField(max_length=100, required=False),
        'enable': forms.NullBooleanField(required=False),
    })
    @fetch_object(CMSRole.objects, 'role')
    @cms_permission_role()
    def post(self, request, role, **kwargs):
        '''
        更新角色信息，要求有权限，且必须是我的下级角色
        :param request:
        :param role:
        :param kwargs:
        :return:
        '''
        params_list = ['name', 'category', 'enable']
        update_param = {}
        for p in params_list:
            if p in kwargs:
                update_param[p] = kwargs[p]
        if len(update_param) > 0:
            CMSRole.objects.filter(id=role.id).update(**update_param)
        return self.success()
