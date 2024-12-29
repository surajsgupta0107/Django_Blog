from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} Your account has been created. You can login now.")
            return redirect("users-login")
    else:
        form = UserRegisterForm()
    context = {
        "title": "Register",
        "block_title": "Register Page",
        "legend": "Register Info",
        "form": form,
    }
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect("users-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "title": "Profile",
        "block_title": "Profile Page",
        "legend": "Profile Info",
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile.html", context)
