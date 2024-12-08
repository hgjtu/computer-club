# Generated by Django 5.1.3 on 2024-12-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='img_path',
            field=models.CharField(default="{% static 'img/no_image.png' %}", max_length=128, verbose_name='Путь до изображения'),
        ),
        migrations.AddField(
            model_name='services',
            name='img_path',
            field=models.CharField(default="{% static 'img/no_image.png' %}", max_length=128, verbose_name='Путь до изображения'),
        ),
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена услуги за час'),
        ),
    ]