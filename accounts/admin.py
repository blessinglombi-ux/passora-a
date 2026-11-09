
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Passora-A Information",
            {
                "fields": (
                    "role",
                    "preferred_language",
                    "email_verified",
                    "phone_number",
                    "profile_picture",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "role",
        "preferred_language",
        "email_verified",
        "is_staff",
    )

    list_filter = (
        "role",
        "preferred_language",
        "email_verified",
        "is_staff",
    )
