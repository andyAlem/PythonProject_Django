from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации пользователей с валидацией полей.
    """
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
