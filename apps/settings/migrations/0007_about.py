# Generated by Django 5.0 on 2023-12-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_settings_work_hours1_settings_work_hours2'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('disc', models.TextField(verbose_name='описание')),
                ('disk_mission', models.TextField(verbose_name='описание миссии')),
                ('disk_prem', models.TextField(verbose_name='описание преймушества')),
                ('disk_gorent', models.TextField(verbose_name='описание гарантии')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
