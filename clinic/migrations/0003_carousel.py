# Generated by Django 4.2.2 on 2024-08-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_department_service_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image_ph', models.ImageField(blank=True, null=True, upload_to='carousel/', verbose_name='Изображение')),
            ],
        ),
    ]
