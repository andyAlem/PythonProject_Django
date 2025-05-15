from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm
from catalog.models import Product


class Contacts(TemplateView):
    """Класс отображения страницы контактов"""

    template_name = "catalog/contacts.html"


class CatalogListView(ListView):
    """Класс отображения списка продуктов."""

    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Класс отображения подробной информации о продукте.
    """

    model = Product
    login_url = reverse_lazy("users:login")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Класс добавления информации о продукте.
    """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:login")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс обновления информации о продукте.
    """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:login")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс удаления информации о продукте.
    """

    model = Product
    success_url = reverse_lazy("catalog:products_list")
    template_name = "catalog/product_delete.html"
    login_url = reverse_lazy("users:login")
