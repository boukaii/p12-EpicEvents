from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "SUPPORT":
            return request.method in ["GET", "PUT"]
        return request.user.team == "Sale"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user == obj.support_contact
                or request.user == obj.contract.sales_contact
            )
        else:
            if obj.cloturer is True:
                raise PermissionDenied("Impossible de mettre à jour un événement terminé.")
            if request.user.team == "SUPPORT":
                return request.user == obj.support_contact
            return request.user == obj.contract.sales_contact
