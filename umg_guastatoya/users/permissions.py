from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to "administrador" profile type users.
    """
    def has_permission(self, request, view):
        return request.user.profile.tipo == 1