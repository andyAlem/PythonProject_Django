from django.shortcuts import HttpResponse, render


def home(request) -> HttpResponse:
    """Функция возвращает страницу home"""

    return render(request, "home.html")


def contacts(request) -> HttpResponse:
    """
    Функция возвращает страницу contacts.html.
    """
    return render(request, "contacts.html")
