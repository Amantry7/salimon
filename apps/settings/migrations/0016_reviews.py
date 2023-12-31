# Generated by Django 5.0 on 2023-12-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_settings_facebook_settings_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dick', models.TextField(verbose_name='отзыв')),
                ('image', models.ImageField(upload_to='fots/', verbose_name='фото клиента')),
                ('client_name', models.CharField(max_length=255, verbose_name='имя клиента')),
                ('servid', models.CharField(max_length=255, verbose_name='какая услуга')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
    ]
