from rest_framework.permissions import BasePermission


class isAdminCanRead(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_superuser
        if request.method == "POST":
            return True