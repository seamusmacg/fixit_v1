from typing import ItemsView
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def save_update(sender, instance, created, **kwargs):
    """Update the order when update/create"""
    print("Save signal received!")
    instance.order.modify_total()


@receiver(post_delete, sender=OrderItem)
def delete_update(sender, instance, **kwargs):
    """Update the order when delete"""
    instance.order.modify_total()


