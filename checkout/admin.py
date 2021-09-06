from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Order, OrderItem

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'overall_cost',)

    fields = ('order_number', 'date', 'name', 'phone', 'email', 'country', 'postcode', 'town', 'address','delivery_cost', 'order_total', 'overall_cost',)

    list_display = ('order_number', 'date', 'name', 'order_total', 'delivery_cost', 'overall_cost',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)