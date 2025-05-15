from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Класс пользователей сайта.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone_number = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    profile_picture = models.ImageField(
        upload_to="users/pictures/", verbose_name="Аватар", blank=True, null=True
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", blank=True, null=True
    )

    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        """
        Настройки модели.
        """

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
