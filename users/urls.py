from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path("register/", views.register, name="users-register"),
    path("profile/", views.profile, name="users-profile"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="users-logout"),
    path("password-reset/",
         auth_views.PasswordResetView.as_view(
             template_name="users/password_reset.html",
             success_url=reverse_lazy("users-password_reset_done"),
             email_template_name="users/password_reset_email.html",
         ),
         name="users-password_reset"),
    path("password-reset/done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="users/password_reset_done.html",
         ),
         name="users-password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html",
             success_url=reverse_lazy("users-password_reset_complete"),
         ),
         name="users-password_reset_confirm"),
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="users/password_reset_complete.html",
         ),
         name="users-password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
