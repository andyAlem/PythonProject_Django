from datetime import date

from django.db import models

from users.models import User


class Category(models.Model):
    """Класс Категорий продукта."""

    name = models.CharField(
        max_length=150,
        verbose_name="Категория продукта",
        help_text="Наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """Класс Продукта"""

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Описание продукта",
    )
    image = models.ImageField(
        upload_to="photos/products",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # SET_NULL
        verbose_name="Категория",
        related_name="products",
        help_text="Категория продукта:",
    )
    price = models.FloatField(
        verbose_name="Цена за покупку",
        help_text="Дата создания",
    )
    created_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Дата создания",
        auto_now_add=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Дата изменения",
        auto_now=True,
    )

    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Опубликовать продукт",
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Создатель",
        related_name="user",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at"]
        permissions = [("can_unpublish_product", "Может отменить публикацию продукта")]
