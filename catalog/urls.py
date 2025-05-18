from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (CatalogListView, Contacts, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductsByCategoryView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="products_list"),
    path(
        "products_by_category/<int:pk>/",
        ProductsByCategoryView.as_view(),
        name="products_by_category",
    ),
    path("contacts/", Contacts.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="products_create"),
    path(
        "catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"
    ),
    path(
        "catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"
    ),
]
