from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict = {
        "title": "Home - Головна",
        "content": "Магазин меблів - HOME",
    }

    return render(request, "main/index.html", context)


def about(request):
    context: dict = {
        "title": "Home - Про нас",
        "content": "Про нас",
        "text_on_page": "Дуже цікавий і потрібний текст тут буде",
    }

    return render(request, "main/about.html", context)
