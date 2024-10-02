from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
        # [
        #     {
        #         "image": "deps/images/goods/sofa.jpg",
        #         "name": "Диван обыкновенный",
        #         "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
        #         "price": 190.00,
        #     },
        #     {
        #         "image": "deps/images/goods/office chair.jpg",
        #         "name": "Стул офисный",
        #         "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
        #         "price": 30.00,
        #     },
        #     {
        #         "image": "deps/images/goods/plants.jpg",
        #         "name": "Растение",
        #         "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
        #         "price": 10.00,
        #     },
        #     {
        #         "image": "deps/images/goods/flower.jpg",
        #         "name": "Цветок стилизированный",
        #         "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
        #         "price": 15.00,
        #     },
        #     {
        #         "image": "deps/images/goods/strange table.jpg",
        #         "name": "Прикроватный столик",
        #         "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
        #         "price": 25.00,
        #     },
        # ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
