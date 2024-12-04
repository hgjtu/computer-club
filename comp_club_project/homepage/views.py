from django.shortcuts import render

component_list = [
    {
        "title": "Ебать какая видюха",   # Видеокарты GeForce RTX 4070 Ti
        "img": "img/homepage/video_card.jpg",
    },
    {
        "title": "Мать в канаве?",   # Материнские платы MSI
        "img": "img/homepage/motherboard.jpg",
    },
    {
        "title": "Проццц?",   # Процессоры Intel Core i7 и AMD Ryzen 9
        "img": "img/homepage/CPU.jpg",
    },
]


games = [
    '1', '2', '3', '4', '5'
]


def index(request):
    template = "homepage/index.html"
    context = {'component_list': component_list,
               'games_count': len(games)}
    return render(request, template, context=context)
