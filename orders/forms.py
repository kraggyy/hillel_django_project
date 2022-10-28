from django import forms
from django.core.exceptions import ValidationError

from products.models import Product


class UpdateCartOrderForm(forms.Form):
    product = forms.UUIDField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.instance = kwargs['instance']

    def clean_product_id(self):
        try:
            product = Product.objects.get(id=self.cleaned_data['product'])
        except Product.DoesNotExist:
            raise ValidationError('Wrong product id.')
        return product

    def save(self, action):
        getattr(self.instance.products, action)(self.cleaned_data['product'])


class RecalculateCartForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.instance = kwargs['instance']
        self.fields = {k: forms.IntegerField() if k.startswith(
            'quantity') else forms.UUIDField() for k in self.data.keys() if
                       k != 'csrfmiddlewaretoken'}

    def save(self):

        for k in self.cleaned_data.keys():
            if k.startswith('product_'):
                index = k.split('_')[-1]
                self.instance.products.through.objects \
                    .filter(product_id=self.cleaned_data[f'product_{index}']) \
                    .update(quantity=self.cleaned_data[f'quantity_{index}'])
        return self.instance
