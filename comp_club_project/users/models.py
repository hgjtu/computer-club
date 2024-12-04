from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class MyUser(AbstractUser):
    birthday = models.DateField('Дата рождения', blank=True)
    phone_num = PhoneNumberField('Номер телефона', blank=True, unique=True)