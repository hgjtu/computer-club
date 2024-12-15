from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    weekday = models.BooleanField(verbose_name='Будний день',
                                  default=True
                                  )
    price = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                verbose_name='Цена услуги за час'
                                )

    def __str__(self):
        return self.title


class Equipment(models.Model):
    type = models.CharField(max_length=128,
                            verbose_name='Тип оборудования',
                            default='Неопределенный тип')
    img_path = models.ImageField(upload_to='equipments/',
                                 default='no_image.png',
                                 verbose_name='Путь до изображения')
    installed_apps_and_games = models.TextField(
        verbose_name='Установленные игры и приложения',
        null=True
        )
    serviceability = models.BooleanField(
        verbose_name='Признак готовности к работе',
        default=True
        )

    def __str__(self):
        return self.type
