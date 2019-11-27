from functools import wraps

from django.http import JsonResponse

from datamodel.models.account import User
from util.code import error


# def cms_auth(function):
#     """
#     管理端用户认证
#     """
#
#     @wraps(function)
#     def decorator(self, request, *args, **kwargs):
#         token = request.META.get('HTTP_X_USER_TOKEN')
#         if not token or AdminUser.objects.filter(token=token).count() <= 0:
#             return JsonResponse({
#                 'code': error.NO_USER
#             })
#         user = AdminUser.objects.get(token=token)
#         if not user.is_enabled:
#             return JsonResponse({
#                 'code': error.USER_DISABLED
#             })
#         # 用户正常
#         request.user = user
#         return function(self, request, *args, **kwargs)
#
#     return decorator


def client_auth(function):
    """
    客户端用户认证
    """

    @wraps(function)
    def decorator(self, request, *args, **kwargs):
        token = request.META.get('HTTP_X_USER_TOKEN')
        if not token or User.objects.filter(token=token).count() <= 0:
            return JsonResponse({
                'code': error.NO_USER
            })
        user = User.objects.get(token=token)
        # if not user.is_enabled:
        #     return JsonResponse({
        #         'code': error.USER_DISABLED
        #     })
        # 用户正常
        request.user = user
        return function(self, request, *args, **kwargs)

    return decorator
