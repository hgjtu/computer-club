# Generated by Django 5.1.3 on 2024-12-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_myuser_img_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='img_path',
            field=models.ImageField(blank=True, default='img/no_image.png', null=True, upload_to='users/profile_photo/', verbose_name='Загрузите фото профиля'),
        ),
    ]
