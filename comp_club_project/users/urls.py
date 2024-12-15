from django.urls import include, path, reverse_lazy
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

from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

app_name = "users"

urlpatterns = [
    path("registration/great_success", views.success_registration, name="great_success"),
    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('users:great_success'),
        ),
        name='registration',
    ),
    path('edit/<str:name>/', views.user_edit, name='edit'),
    path("profile/<str:name>/", views.user_profile, name="profile"),
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
