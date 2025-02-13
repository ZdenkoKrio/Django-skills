from django.urls import path, include
from .views import RegisterView, ProfileView, SettingsView, ProfileUpdateView
from .auth_urls import auth_patterns

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("settings/", SettingsView.as_view(), name="settings"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_update"),
    path("", include(auth_patterns)),
]