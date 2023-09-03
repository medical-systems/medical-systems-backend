from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserInsurance, UserRole, UserGender


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "role",
        "email",
        "first_name",
        "last_name",
    ]
    fieldsets = (
    ("User Information", {
        "fields": ("username", "email", "password"),
    }),
    ("Personal Info", {
        "fields": ("first_name", "last_name", "date_of_birth", "gender", "phone_num", "insurance"),
    }),
    ("Permissions", {
        "fields": ("role", "about_doctor", "is_active", "is_staff", "is_superuser"),
    }),
    ("Important Dates", {
        "fields": ("last_login", "date_joined"),
    }),
)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserRole)
admin.site.register(UserInsurance)
admin.site.register(UserGender)
