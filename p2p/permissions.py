from rest_framework import permissions


class Buy(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action in ["update", "partial_update"]:
            return False

        if view.action == "destroy":
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == "create":
            return request.user.is_authenticated

        return True


class Sell(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action in ["update", "partial_update"]:
            return False

        if view.action == "destroy":
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == "create":
            return request.user.is_authenticated

        return True


class Trade(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action in ["update", "partial_update"]:
            return False

        if view.action == "destroy":
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == "create":
            return request.user.is_authenticated

        return True
