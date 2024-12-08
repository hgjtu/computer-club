# Generated by Django 5.1.3 on 2024-12-08 16:25

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, default='', verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_num',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None, verbose_name='Номер телефона'),
        ),
    ]