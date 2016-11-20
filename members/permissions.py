from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):


    def has_permission(self, request, view):
        print(request.method)
        print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        print(request.user.is_superuser)
        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
