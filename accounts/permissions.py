from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAccountOwnerOrSecretary(BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user.id == obj.id or request.user.role.role_name == "Secretary"
