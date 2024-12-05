from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    img_path = models.CharField(max_length=128,
                                verbose_name='Путь до изображения',
                                default="{% static 'img/no_image.png' %}",
                                )
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена услуги за час'
                                )

    def __str__(self):
        return self.title


class Equipment(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    img_path = models.CharField(max_length=128,
                                verbose_name='Путь до изображения',
                                default="{% static 'img/no_image.png' %}",
                                )
    installed_apps_and_games = models.TextField(
        verbose_name='Установленные игры и приложения'
        )
    
    def __str__(self):
        return self.title
