from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class MyUser(AbstractUser):
    birthday = models.DateField('Дата рождения', blank=True, null=True,
                                help_text="Мы Вас поздравим и сделаем скидку :)",
                                )
    phone_num = PhoneNumberField('Номер телефона', blank=True)
    img_path = models.ImageField(upload_to='users/profile_photo/',
                                 default='no_image.png',
                                 verbose_name='Загрузите фото профиля',
                                 blank=True, null=True)
