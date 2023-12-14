# Generated by Django 5.0 on 2023-12-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='фото')),
                ('names', models.CharField(max_length=255, verbose_name='имя сотрудника')),
                ('rols', models.CharField(max_length=255, verbose_name='роль сотрудника')),
                ('diks', models.TextField(verbose_name='мини описание')),
                ('diks2', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Cотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]