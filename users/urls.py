from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

from users.views import (
    activation_view,
    get_user_detail,
    get_user_list,
    profile_view,
    signup,
)


app_name = "users"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            template_name="users/login.html",
            next_page=reverse_lazy("users:login"),
        ),
        name="logout",
    ),
    path(
        "password_change/",
        PasswordChangeView.as_view(
            template_name="users/passwd_change.html",
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="users/passwd_change_done.html",
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="users/passwd_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="users/passwd_reset.html",
            success_url=reverse_lazy("users:password_reset_done"),
            email_template_name="users/email.html",
        ),
        name="password_reset",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/passwd_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="users/passwd_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("signup/", signup, name="signup"),
    path("activate/<str:username>/", activation_view, name="activation_view"),
    path("profile/", profile_view, name="profile"),
    path("active_users/", get_user_list, name="active_users"),
    path(
        "user_detail/<int:id>/",
        get_user_detail,
        name="user_detail",
    ),
]
