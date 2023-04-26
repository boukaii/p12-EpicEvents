from django.utils import timezone
from rest_framework import permissions
from events.models import Event
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "SUPPORT":
            return request.method in ["GET", "PUT"]
        return request.user.team == "SALES"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user == obj.support_contact
                or request.user == obj.contract.sales_contact
            )
        else:
            if obj.cloturer is True:
                raise PermissionDenied("Cannot update a finished event.")
            if request.user.team == "SUPPORT":
                return request.user == obj.support_contact
            return request.user == obj.contract.sales_contact







# from django.utils import timezone
# from rest_framework import permissions
# from events.models import Event
# from rest_framework.permissions import BasePermission, SAFE_METHODS
# #
#
# class IsSupportEmployeeOrReadOnly(permissions.BasePermission):
#     message = "Le support ne peut lire que les données"
#
#     def has_permission(self, request, view):
#         if request.method == 'POST' and request.user.team == 'SUPPORT':
#             return False
#         return True
#
#
# class IsEventFinish(permissions.BasePermission):
#     message = "Une fois l'event cloturer il ne peut etre mis a jour."
#
#     def has_permission(self, request, view):
#
#         return request.user and request.user.is_authenticated
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.event_date > timezone.now()
#
#
# # class IsSaleEmployeeConnectedToTheEventOrReadOnly(permissions.BasePermission):
#     # message = "Uniquement réserver au employer sur l'event en question"
#     #
#     # def has_permission(self, request, view):
#     #
#     #     return request.user and request.user.is_authenticated
#
#     # def has_object_permission(self, request, view, obj):
#     #
#     #     if request.method in permissions.SAFE_METHODS:
#     #         return True
#     #
#     #     return obj.contract.client.support_contact == request.user
#
# class IsSaleEmployeeConnectedToTheEventOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.team == "Support":
#             return True
#         else:
#             return False
#
#     def has_object_permission(self, request, view, obj):
#         if request.user.team == "Support":
#             if type(obj) == Event:
#                 if obj.support_contact == request.user:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
