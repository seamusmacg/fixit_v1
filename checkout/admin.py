from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    """OrderItem Admin Class"""
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    """Order Admin Class"""

    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total', 'overall_cost',)

    fields = ('order_number', 'user_profile', 'date', 'name', 'phone', 'email', 'country',
              'postcode', 'town', 'address', 'delivery_cost', 'order_total', 'overall_cost',)

    list_display = ('order_number', 'date', 'name',
                    'order_total', 'delivery_cost', 'overall_cost',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
