# Generated by Django 5.0 on 2023-12-15 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0018_settings_clints_settings_hours_work_settings_ofise_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='ofise',
            new_name='office',
        ),
    ]
