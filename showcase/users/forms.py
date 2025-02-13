from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
)
from .models import CustomUser
from core.forms import BaseForm


class CustomUserCreationForm(UserCreationForm, BaseForm):
    submit_text = "Sign Up"

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "role"]


class CustomAuthenticationForm(AuthenticationForm, BaseForm):
    submit_text = "Login"


class CustomPasswordChangeForm(PasswordChangeForm, BaseForm):
    submit_text = "Change Password"


class CustomPasswordResetForm(PasswordResetForm, BaseForm):
    submit_text = "Send Reset Link"


class UserUpdateForm(forms.ModelForm, BaseForm):
    submit_text = "Save Changes"

    class Meta:
        model = CustomUser
        fields = ["username", "email", "profile_picture", "bio"]