from rest_framework import permissions
from .models import Product


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            return True
        return False
        
    