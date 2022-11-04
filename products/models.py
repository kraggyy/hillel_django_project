from os import path

from django.core.cache import cache
from django.db import models
from django_lifecycle import hook, AFTER_DELETE, AFTER_SAVE

from shop.constants import MAX_DIGITS, DECIMAL_PLACES
from shop.mixins.models_mixins import PKMixin
from shop.model_choices import Currency


def upload_image(instance, filename):
    _name, extension = path.splitext(filename)
    return f'images/{instance.__class__.__name__.lower()}/' \
           f'{instance.pk}/image{extension}'


class Category(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image)

    def __str__(self):
        return f'{self.name} | {self.description}'


class Product(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image)
    category = models.ForeignKey(
        "products.Category",
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0
    )
    sku = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )
    products = models.ManyToManyField('products.Product', blank=True)

    def __str__(self):
        return f'{self.name} | {self.price} | {self.sku}'

    @classmethod
    def _cache_key(self):
        return 'products'

    @classmethod
    def get_products(cls):
        products = cache.get(cls._cache_key())
        if not products:
            products = Product.objects.all()
            cache.set(cls._cache_key(), products)
        return products

    @hook(AFTER_SAVE)
    @hook(AFTER_DELETE)
    def clear_products_cache(self):
        cache.delete(self._cache_key())
