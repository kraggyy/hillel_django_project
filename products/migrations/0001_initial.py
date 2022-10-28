# Generated by Django 3.2.15 on 2022-10-28 18:04

from django.db import migrations, models
import django.db.models.deletion
import products.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)), # noqa
                ('created_at', models.DateTimeField(auto_now_add=True)), # noqa
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=products.models.upload_image)), # noqa
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)), # noqa
                ('created_at', models.DateTimeField(auto_now_add=True)), # noqa
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=products.models.upload_image)), # noqa
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)), # noqa
                ('sku', models.CharField(blank=True, max_length=32, null=True)), # noqa
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')), # noqa
                ('products', models.ManyToManyField(blank=True, to='products.Product')), # noqa
            ],
            options={
                'abstract': False,
            },
        ),
    ]
