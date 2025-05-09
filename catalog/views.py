from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.models import Product


class Contacts(TemplateView):
    """Класс отображения страницы контактов"""

    template_name = "catalog/contacts.html"


class CatalogListView(ListView):
    """Класс отображения списка продуктов."""

    model = Product


class ProductDetailView(DetailView):
    """
    Класс отображения подробной информации о продукте.
    """

    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    """
    Класс добавления информации о продукте.
    """

    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    """
    Класс обновления информации о продукте.
    """

    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    """
    Класс удаления информации о продукте.
    """

    model = Product
    success_url = reverse_lazy("catalog:products_list")
    template_name = "catalog/product_delete.html"
