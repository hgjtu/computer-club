from django.shortcuts import render
from django.db import connection

component_list = [
    {
        "title": "Видеокарты GeForce RTX 4070 Ti",
        "img": "img/homepage/video_card.jpg",
    },
    {
        "title": "Материнские платы MSI",
        "img": "img/homepage/motherboard.jpg",
    },
    {
        "title": "Процессоры Intel Core i7 и AMD Ryzen 9",
        "img": "img/homepage/CPU.jpg",
    },
]


def index(request):
    template = "homepage/index.html"
    games = set()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT installed_apps_and_games \
            FROM services_equipment_equipment"
            )
        rows = cursor.fetchall()
    for row in rows:
        games.update(row[0].split(", "))
    context = {'component_list': component_list,
               'games_count': len(games)}
    return render(request, template, context=context)
