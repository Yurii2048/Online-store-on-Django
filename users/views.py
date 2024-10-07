from django.shortcuts import render


def login(request):
    context = {
        "title": "Home - Авторизація",
    }
    return render(request, "users/login.html", context)


def registration(request):
    context = {
        "title": "Home - Реєстрація",
    }
    return render(request, "users/registration.html", context)


def profile(request):
    context = {
        "title": "Home - Особистий кабінет",
    }
    return render(request, "users/profile.html", context)


def logout(request):
    pass