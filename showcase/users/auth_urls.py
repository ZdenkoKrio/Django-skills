from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import (
    CustomAuthenticationForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm
)

auth_patterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="components/form_component.html",
        authentication_form=CustomAuthenticationForm,
        extra_context={"title": "Login", "description": "Enter your credentials to access your account."}
    ), name="login"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name="components/form_component.html",
        form_class=CustomPasswordChangeForm,
        extra_context={"title": "Change Password", "description": "Update your password for better security."}
    ), name="password_change"),

    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="users/password_change_done.html"
    ), name="password_change_done"),

    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="components/form_component.html",
        form_class=CustomPasswordResetForm,
        extra_context={"title": "Reset Password", "description": "Enter your email to receive a password reset link."}
    ), name="password_reset"),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="components/form_component.html",
        extra_context={"title": "Set New Password", "description": "Enter your new password."}
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html"
    ), name="password_reset_complete"),
]