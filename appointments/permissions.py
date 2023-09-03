from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAppointmentOwnerOrSecretary(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.patient == request.user or obj.doctor == request.user or request.user.role.role_name == "Secretary":
                return True
        return False
