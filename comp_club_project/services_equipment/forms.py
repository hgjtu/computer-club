from django import forms
from .models import Services, Equipment


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'weekday', 'price']
        labels = {
            'title': 'Название',
            'weekday': 'Будний день',
            'price': 'Цена услуги за час',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'weekday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['img_path', 'type',
                  'installed_apps_and_games', 'serviceability']
        labels = {
            'type': 'Тип оборудования',
            'installed_apps_and_games': 'Установленные игры и приложения',
            'serviceability': 'Признак готовности к работе',
        }
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'installed_apps_and_games': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
                ),
            'serviceability': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
                ),
        }
