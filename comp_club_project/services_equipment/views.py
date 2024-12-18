from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from .models import Services, Equipment
from .forms import ServicesForm, EquipmentForm
import os
from django.core.files import File
from django.conf import settings


def delete_equipment(request, equip_id):
    if request.method == 'POST':
        equipment = get_object_or_404(Equipment, id=equip_id)
        equipment.delete()
        return redirect('serv_equip:serv_equip_main')


def ServicedEquipment(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'service':
            service_id = request.POST.get('service_id')
            service = get_object_or_404(Services, id=service_id)
            form = ServicesForm(request.POST, instance=service)
            if form.is_valid():
                form.save()

        elif form_type == 'equipment':
            equipment_id = request.POST.get('equipment_id')
            equip = get_object_or_404(Equipment, id=equipment_id)
            form = EquipmentForm(request.POST, request.FILES, instance=equip)
            if form.is_valid():
                if (form.cleaned_data['img_path'] is False):
                    with open(os.path.join(settings.BASE_DIR,
                                           'media/no_image.png'), 'rb') as f:
                        form.instance.img_path.save('no_image.jpg', File(f))
                form.save()

    equipments = Equipment.objects.order_by('id')
    services = Services.objects.order_by('weekday').reverse()

    if request.method == 'GET':
        title = request.GET.get('title', '')
        weekday = request.GET.get('weekday', '')
        price = request.GET.get('price', '')
        equip_type = request.GET.get('type', '')
        installed_apps = request.GET.get('installed_apps_and_games', '')

        if title:
            services = services.filter(title__icontains=title)
        if weekday:
            weekday_filter = True if weekday == 'yes' else False
            services = services.filter(weekday=weekday_filter)
        if price:
            try:
                services = services.filter(price__lte=float(price))
            except ValueError:
                pass

        if equip_type:
            equipments = equipments.filter(type__icontains=equip_type)
        if installed_apps:
            equipments = equipments.filter(
                installed_apps_and_games__icontains=installed_apps
                )

    for equipment in equipments:
        equipment.form = EquipmentForm(instance=equipment)
        equipment.installed_apps_and_games \
            = equipment.installed_apps_and_games.replace(",", ", ")

    for service in services:
        service.form = ServicesForm(instance=service)

    template = "serv_equip/serv_equip_main.html"

    context = {
        'services': services,
        'equipment': equipments,
    }

    return render(request, template, context=context)
