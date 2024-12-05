from django.urls import path
from . import views

app_name = 'serv_equip'

urlpatterns = [
    path('',  views.ServicedEquipment, name='serv_equip_main'),
]
