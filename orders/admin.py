

from django.contrib import admin

from orders.models import Order, Discount


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('discounted',)
    list_display = ('id', 'user', 'total_amount', 'discount', 'discounted')
    filter_horizontal = ('products',)

    def discounted(self, obj=None):
        return obj.get_total_amount()

    discounted.short_description = 'Total amount include discount'


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_filter = ('discount_type', 'is_active')