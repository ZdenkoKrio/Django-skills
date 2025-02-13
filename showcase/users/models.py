from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ("admin", "Admin"),
        ("editor", "Editor"),
        ("viewer", "Viewer"),
    ], default="viewer")

    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            ("can_edit_articles", "Can edit articles"),
            ("can_delete_users", "Can delete users"),
        ]
