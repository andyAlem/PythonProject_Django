from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product
from constants import BANNED_WORDS


class ProductForm(ModelForm):
    """
    Форма для добавления и редактирования продукта.
    """

    class Meta:
        model = Product
        exclude = ("view_counter",)

    def __init__(self, *args, **kwargs):
        """
        Привязывает стили к полям формы
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_name(self):
        """
        Проверяет, не содержит ли поле запрещенных слов в названии продукта
        """
        name = self.cleaned_data.get("name")
        for word in BANNED_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'Поле содержит запрещенное слово - "{word}"')
        return name

    def clean_description(self):
        """
        Проверяет, не содержит ли поле запрещенных слов в описании продукта
        """
        description = self.cleaned_data.get("description")
        for word in BANNED_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'Поле содержит запрещенное слово - "{word}"')
        return description

    def clean_price(self):
        """
        Проверяет, не является ли поле цены отрицательной
        """
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price


class CatalogModeratorForm(ModelForm):
    """
    Форма для модератора каталога.
    """

    class Meta:
        model = Product
        fields = ["is_published"]
