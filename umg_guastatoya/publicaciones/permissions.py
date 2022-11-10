from rest_framework.permissions import BasePermission


class IsAdminOrPublisher(BasePermission):
    """
    If the request is GET then it will give acces to the endpoint
    Allows access only to "administrador" and "publicador" profile type users.
    """
    def has_permission(self, request, view):
        if request.method == 'GET': return True
        return request.user.profile.tipo == 1 or request.user.profile.tipo == 4