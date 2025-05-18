from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Возвращает список продуктов из кэша или из базы данных."""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)

    if products is None:
        products = Product.objects.all()
        cache.set(key, products)
        return products

    return products


def get_products_by_category(pk):
    """Возвращает список продуктов по категории pk"""
    return Product.objects.filter(category_id=pk)
