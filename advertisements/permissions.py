from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.creator