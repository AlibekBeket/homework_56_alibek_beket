# Generated by Django 4.1.7 on 2023-02-27 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('product_description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание товара')),
                ('product_image', models.TextField(verbose_name='Фото товара')),
                ('category', models.TextField(choices=[('other', 'Разное'), ('food', 'Еда'), ('electronics', 'Электроника'), ('cars', 'Автомобили')], default='other', verbose_name='Категория')),
                ('the_rest_of_the_goods', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
            ],
        ),
    ]
