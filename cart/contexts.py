from decimal import Decimal
from django.conf import settings 

def cart_contents(request):

    cart_items = []
    total = 0 
    product_count = 0 

    if total < settings.FREE_DELIVERY_CONDITION:
        delivery_cost = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_CONDITION - total
    else:
        delivery_cost = 0
        free_delivery_delta = 0

    overall_cost = delivery_cost + total


    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost, 
        'free_delivery_delta': free_delivery_delta, 
        'free_delivery_condition': settings.FREE_DELIVERY_CONDITION, 
        'grand_total': overall_cost, 

    }

    return context