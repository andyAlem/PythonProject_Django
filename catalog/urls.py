from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (CatalogListView, Contacts, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="products_list"),
    path("contacts/", Contacts.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="products_create"),
    path(
        "catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"
    ),
    path(
        "catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"
    ),
]
