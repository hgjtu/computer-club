from django.urls import path
from . import views

app_name = 'serv_equip'

urlpatterns = [
    path('',  views.ServicedEquipment, name='serv_equip_main'),
    path('equipment/delete/<int:equip_id>/', views.delete_equipment,
         name='delete_equipment')
]
