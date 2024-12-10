from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from services_equipment.models import Services, Equipment
from django.core.exceptions import ValidationError


class MyUser(AbstractUser):
    birthday = models.DateField('Дата рождения', blank=True, null=True,
                                help_text="Мы Вас поздравим и сделаем скидку :)",
                                )
    phone_num = PhoneNumberField('Номер телефона', blank=True)
    img_path = models.ImageField(upload_to='users/profile_photo/',
                                 default='no_image.png',
                                 verbose_name='Загрузите фото профиля',
                                 blank=True)


class Session(models.Model):
    start_time = models.DateTimeField("Дата и время начала",
                                      null=False, auto_now_add=True)
    end_time = models.DateTimeField("Дата и время окончания", null=True)
    user_id = models.ForeignKey(
        MyUser,
        verbose_name="Номер пользователя",
        on_delete=models.CASCADE,
        null=False,
    )
    service_id = models.ForeignKey(
        Services,
        verbose_name="Номер услуги",
        on_delete=models.CASCADE,
        null=False,
    )
    equipment_id = models.ForeignKey(
        Equipment,
        verbose_name="Номер оборудования",
        on_delete=models.CASCADE,
        null=False,
    )

    def save(self, *args, **kwargs):
        if Session.objects.filter(equipment_id=self.equipment_id,
                                  end_time__isnull=True).exists():
            raise ValidationError("Нельзя добавить запись: \
                                  оборудование уже используется.")
        super().save(*args, **kwargs)
