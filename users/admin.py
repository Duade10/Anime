from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
        "login_method",
        "type",
        "age_group",
    )
    list_filter = ("type", "age_group", "login_method")
    fieldsets = UserAdmin.fieldsets + (("Custom User Fields", {"fields": ("login_method", "type", "age_group")}),)
    search_fields = ("username__icontains", "first_name")
