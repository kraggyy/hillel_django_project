# Generated by Django 3.2.15 on 2022-10-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('amount', models.PositiveIntegerField()),
                ('code', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('discount_type', models.PositiveSmallIntegerField(choices=[(0, 'In money'), (1, 'In percent')])), # noqa
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('price', models.PositiveIntegerField()),
                ('sku', models.CharField(max_length=64)),
            ],
        ),
    ]
