import secrets

from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER

from users.forms import UserRegisterForm
from users.models import User


class CustomLogoutView(LogoutView):
    """
    Класс выхода из системы.
    """

    def dispatch(self, request, *args, **kwargs):
        message = "Вы вышли из системы"
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    """
    Класс добавления нового пользователя.
    """

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Подтверждение регистрации",
            message=f"Для подтверждения регистрации перейдите по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    """
    Подтверждение регистрации по токену.
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
