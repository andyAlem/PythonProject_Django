from django.shortcuts import HttpResponse, get_object_or_404, render

from catalog.models import Product


def contacts(request) -> HttpResponse:
    """
    Функция возвращает страницу contacts.html.
    """
    return render(request, "contacts.html")


def products_list(request):
    """
    :param request:
    :return:
    """
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context=context)


def products_detail(request, pk):
    """
    Рендеринг одного товара
    :param request:
    :param pk:
    :return:
    """
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context=context)
