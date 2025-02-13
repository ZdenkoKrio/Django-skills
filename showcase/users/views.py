from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "settings.html"


@permission_required("users.can_edit_articles")
def edit_articles(request):
    return render(request, "edit_articles.html")


@login_required
def assign_role(request, user_id, role):
    user = CustomUser.objects.get(id=user_id)
    user.role = role
    user.save()
    return redirect("profile")


@login_required
def assign_group(request, user_id, group_name):
    user = CustomUser.objects.get(id=user_id)
    group, created = Group.objects.get_or_create(name=group_name)
    user.groups.add(group)
    return redirect("profile")