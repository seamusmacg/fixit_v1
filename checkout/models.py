import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField
from profiles.models import Profile


class Order(models.Model):
    """Order model"""
    order_number = models.CharField(max_length=255, null=False, editable=False)
    user_profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=350, null=False, blank=False)
    phone = models.CharField(max_length=18, null=False, blank=False)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    town = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    overall_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _create_order_number(self):
        """Create order number"""
        return uuid.uuid4().hex[:10].upper()

    def modify_total(self):
        """Calculate/modify the total"""
        self.order_total = self.items.aggregate(Sum('item_total'))[
            'item_total__sum'] or 0
        free_delivery = self.order_total > settings.FREE_DELIVERY_CONDITION
        if free_delivery:
            self.delivery_cost = 0
        else:
            self.delivery_cost = self.order_total * settings.DELIVERY_PERCENTAGE / 100
        self.overall_cost = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """Save order"""
        if not self.order_number:
            self.order_number = self._create_order_number()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """Orderitem model"""
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """Save Orderitem"""

        self.item_total = self.product.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'Product Code {self.product.sku} on order {self.order.order_number}'
