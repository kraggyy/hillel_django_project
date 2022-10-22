import csv
import decimal

import codecs
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from products.models import Product, Category


class ImportCSVForm(forms.Form):
    file = forms.FileField(
        validators=[FileExtensionValidator(['csv'])]
    )

    def clean_file(self):
        csv_file = self.cleaned_data['file']
        reader = csv.DictReader(codecs.iterdecode(csv_file, 'utf-8'))
        products_list = []
        for product in reader:
            try:
                products_list.append(
                    Product(
                        name=product['name'],
                        description=product['description'],
                        price=decimal.Decimal(product['price']),
                        sku=product['sku'],
                        category=Category.objects.get_or_create(
                            name=product['category']
                        )[0]
                    )
                )
            except (KeyError, decimal.InvalidOperation) as err:
                raise ValidationError(err)
        if not products_list:
            raise ValidationError('Wrong file format.')
        return products_list

    def save(self):
        Product.objects.bulk_create(self.cleaned_data['file'])
