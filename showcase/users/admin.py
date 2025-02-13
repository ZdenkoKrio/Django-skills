from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = ("username", "email", "role", "is_active", "is_staff", "date_joined")
    list_filter = ("role", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "email")
    ordering = ("date_joined",)

    fieldsets = (
        ("User Information", {"fields": ("username", "email", "password")}),
        ("Profile Details", {"fields": ("profile_picture", "bio", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        ("Create User", {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "role", "is_active", "is_staff", "is_superuser"),
        }),
    )

    readonly_fields = ("date_joined", "last_login")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by("-date_joined")