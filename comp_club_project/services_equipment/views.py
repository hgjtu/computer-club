from django.shortcuts import render

from django.views.generic import TemplateView


class ServicedEquipment(TemplateView):
    template_name = "serv_equip/serv_equip_main.html"
