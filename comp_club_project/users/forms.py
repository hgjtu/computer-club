from django import forms
from .models import MyUser


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password', 'first_name',
                  'last_name', 'birthday', 'phone_num', 'email']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
