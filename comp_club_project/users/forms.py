from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['img_path', 'username', 'first_name',
                  'last_name', 'birthday', 'phone_num', 'email']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'email',)
