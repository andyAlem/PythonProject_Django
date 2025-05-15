from django.db import models


class Blog(models.Model):
    """Класс Блога."""

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое", help_text="Текст блога")
    image = models.ImageField(
        upload_to="photos/blogs", verbose_name="Изображение", blank=True, null=True
    )
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Дата создания", auto_now_add=True
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Дата изменения",
        auto_now=True,
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "is_published", "created_at", "updated_at", "views_count"]
