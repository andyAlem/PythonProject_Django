from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import CatalogModeratorForm, ProductForm
from catalog.models import Category, Product
from catalog.services import get_products_by_category, get_products_from_cache


class Contacts(TemplateView):
    """Класс отображения страницы контактов"""

    template_name = "catalog/contacts.html"


class CatalogListView(ListView):
    """Класс отображения списка продуктов."""

    model = Product

    def get_queryset(self):
        """Возвращает список продуктов с учетом кэширования."""
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Класс отображения подробной информации о продукте."""

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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования информации о продукте."""

    model = Product
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:login")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj

    def get_form_class(self):
        user = self.request.user
        obj = self.get_object()
        if user == obj.owner:
            return ProductForm
        elif user.has_perm("catalog.can_unpublish_product"):
            return CatalogModeratorForm
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления продукта."""

    model = Product
    success_url = reverse_lazy("catalog:products_list")
    template_name = "catalog/product_delete.html"
    login_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = self.request.user
        if obj.owner != user and not user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ProductsByCategoryView(ListView):
    """Класс отображения продуктов по категории."""

    model = Product
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("pk")
        context["category"] = Category.objects.get(pk=category_id)
        return context
