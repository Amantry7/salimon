# Generated by Django 5.0 on 2023-12-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_settings_options_rename_we_name_settings_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='work_hours1',
            field=models.CharField(default=1, max_length=255, verbose_name='рабочие время в будние'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='work_hours2',
            field=models.CharField(default=1, max_length=255, verbose_name='рабочие время в выходные'),
            preserve_default=False,
        ),
    ]
