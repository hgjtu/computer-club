from django.shortcuts import render

from .models import Services, Equipment


def ServicedEquipment(request):
    equipments = Equipment.objects.order_by('id')
    for equipment in equipments:
        equipment.installed_apps_and_games = equipment.installed_apps_and_games.replace(",", ", ")

    template = "serv_equip/serv_equip_main.html"
    context = {'services': Services.objects.order_by('weekday').reverse,
               'equipment': equipments}
    return render(request, template, context=context)
