# Generated by Django 5.1.3 on 2024-12-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_myuser_img_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, help_text='Мы Вас поздравим и сделаем скидку :)', verbose_name='Дата рождения'),
        ),
    ]