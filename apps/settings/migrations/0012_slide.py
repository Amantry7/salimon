# Generated by Django 5.0 on 2023-12-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_employee_photo1_employee_photo2_employee_photo3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя сайта')),
                ('discriptions', models.CharField(max_length=255, verbose_name='описание')),
                ('photos', models.ImageField(upload_to='photos/', verbose_name='фото')),
            ],
        ),
    ]
