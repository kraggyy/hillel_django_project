from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db import models

from shop.constants import MAX_DIGITS, DECIMAL_PLACES
from shop.mixins.models_mixins import PKMixin
from shop.model_choices import DiscountTypes


class Discount(PKMixin):
    amount = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0
    )
    code = models.CharField(
        max_length=32
    )
    is_active = models.BooleanField(
        default=True
    )
    discount_type = models.PositiveSmallIntegerField(
        choices=DiscountTypes.choices,
        default=DiscountTypes.VALUE
    )


class Order(PKMixin):
    total_amount = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    products = models.ManyToManyField("items.Product")
    discount = models.ForeignKey(Discount,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True
                                 )  # noqa

    def amount_with_discount(self):
        if self.discount is True:
            if self.discount.discount_type == DiscountTypes.VALUE:
                return (self.total_amount - self.discount.amount).quantize(
                    Decimal('.00'))
            elif self.discount.discount_type == DiscountTypes.PERCENT:
                return self.total_amount - (self.total_amount * (
                        self.discount.amount / 100)).quantize(
                    Decimal('.00'))
        return self.total_amount

    def __str__(self):
        return f'{self.amount_with_discount()}'
