# Generated by Django 5.0 on 2023-12-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_servides'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='facebook',
            field=models.URLField(default=1, verbose_name='Facebook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='instagram',
            field=models.URLField(default=1, verbose_name='instagram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='linkedin',
            field=models.URLField(default=1, verbose_name='linkedin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='skype',
            field=models.URLField(default=1, verbose_name='skype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='twitter',
            field=models.URLField(default=1, verbose_name='Twitter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='youtube',
            field=models.URLField(default=1, verbose_name='youtube'),
            preserve_default=False,
        ),
    ]
