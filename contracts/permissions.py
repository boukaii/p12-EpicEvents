from rest_framework import permissions


class IsSaleEmployeeConnectedToTheContractOrReadOnly(permissions.BasePermission):
    message = "Vous pouvez mettre à jour un contrat uniquement si vous y êtes affecté"

    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.client.sales_contact == request.user


class IsSupportEmployeeOrReadOnly(permissions.BasePermission):
    message = "Seul le support peut lire les données"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.team == 'SUPPORT':
            return False
        return True
