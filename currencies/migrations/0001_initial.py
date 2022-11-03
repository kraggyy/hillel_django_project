# Generated by Django 3.2.15 on 2022-11-03 15:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)), # noqa
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=3)), # noqa
                ('buy', models.DecimalField(decimal_places=2, default=1, max_digits=8)), # noqa
                ('sale', models.DecimalField(decimal_places=2, default=1, max_digits=8)), # noqa
            ],
            options={
                'abstract': False,
            },
        ),
    ]
