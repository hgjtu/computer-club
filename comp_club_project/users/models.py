from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class MyUser(AbstractUser):
    birthday = models.DateField('Дата рождения', blank=False,
                                help_text="Обязательное поле.",
                                )
    phone_num = PhoneNumberField('Номер телефона', blank=True)
    img_path = models.CharField(max_length=128,
                                verbose_name='Путь до изображения',
                                default='img/no_image.png',
                                )
