# Generated by Django 5.0 on 2023-12-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_alter_slide_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servides', models.CharField(max_length=255, verbose_name='название услуги')),
                ('dirs', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
            },
        ),
    ]