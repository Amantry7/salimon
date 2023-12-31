# Generated by Django 5.0 on 2023-12-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0016_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='phot', verbose_name='фото')),
                ('name', models.CharField(max_length=255, verbose_name='название поста')),
                ('description', models.CharField(max_length=255, verbose_name='опицание')),
                ('data', models.CharField(max_length=255, verbose_name='день публикатци')),
                ('mount', models.CharField(max_length=255, verbose_name='месяц публикатци')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]
