# Generated by Django 3.2.15 on 2022-12-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221228_1805'),
        ('favourites', '0002_favourites_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='products',
            field=models.ManyToManyField(related_name='in_favourites', to='products.Product'),
        ),
    ]