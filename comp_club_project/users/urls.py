from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

app_name = "users"

urlpatterns = [
    # path("create/", views.user, name="create"),
    path('edit/', views.user, name='edit'),
    path("profile/", views.user_profile, name="profile"),
    # Логин.
    path(
        "login/",
        LoginView.as_view(template_name="registration/logged_in.html"),
        name="login",
    ),
    # Логаут.
    path(
        "logout/",
        LogoutView.as_view(template_name="registration/logged_out.html"),
        name="logout",
    ),
    # Изменение пароля.
    path("password_change/", PasswordChangeView.as_view(),
         name="password_change"),
    # Сообщение об успешном изменении пароля.
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # Восстановление пароля.
    path("password_reset/", PasswordResetView.as_view(),
         name="password_reset"),
    # Сообщение об отправке ссылки для восстановления пароля.
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    # Вход по ссылке для восстановления пароля.
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # Сообщение об успешном восстановлении пароля.
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
