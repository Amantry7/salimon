# Generated by Django 5.0 on 2023-12-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_slide_image_alter_slide_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_name', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='логотип')),
                ('namber', models.CharField(max_length=255, verbose_name='номер телефона')),
                ('what_number', models.CharField(max_length=255, verbose_name='ватпсап номер')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
    ]