from django.shortcuts import render


def ServicedEquipment(request):
    template = "serv/equip_main.html"
    context = {'services': services,
               'equipment': equipment}
    return render(request, template, context=context)
