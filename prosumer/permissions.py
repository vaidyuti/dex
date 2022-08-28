from rest_framework import permissions


class Prosumer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action in ["update", "partial_update"]:
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == "create":
            return request.user.is_authenticated

        return True
