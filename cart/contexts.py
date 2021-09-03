from django.conf import settings
from collections import Counter
from django.shortcuts import get_object_or_404 
from products.models import Product



def calculate_delivery_cost(total):
    """Calculate delivery cost

    Args:
        Total (Integer): Total cost of products

    Returns:
        Delivery Cost [Integer]: Delivery cost of order
    """
    free_delivery = total > settings.FREE_DELIVERY_CONDITION 
    if free_delivery:
        delivery_cost = 0
    else:
        delivery_cost = total * settings.FREE_DELIVERY_CONDITION / 100
    
    return delivery_cost


def calculate_delivery_delta(total):
    """Calculate free delivery delta of

    Args:
        total (Integer): Total cost of products

    Returns:
       Free delivery delta [Integer] : Free delivery delta
    """
    free_delivery = total > settings.FREE_DELIVERY_CONDITION
    if free_delivery:
        free_delivery_remainder = 0
    else:
        free_delivery_remainder = settings.FREE_DELIVERY_CONDITION - total

    return free_delivery_remainder



def cart_contents(request):
    """Get cart contents

    Args:
        request (GET request ): Get Cart from session

    Returns:
        [Dictionary]: Context dictionary of cart items
    """

    cart_list = []
    total = 0 
    product_count = 0
    product_quantity = 0
    cart = request.session.get('cart', {})


    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        product_quantity = quantity + product_quantity
        total += quantity * product.price
        product_count += product.price
        cart_list += [{'product_id': product_id, 'quantity': quantity, 'product': product,}]

    delivery_cost = calculate_delivery_cost(total)
    free_delivery_remainder = calculate_delivery_delta(total)

    overall_cost = delivery_cost + total



    context = {
        'cart_list': cart_list,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost, 
        'free_delivery_remainder': free_delivery_remainder, 
        'free_delivery_condition': settings.FREE_DELIVERY_CONDITION, 
        'overall_cost': overall_cost, 
        'product_quantity': product_quantity,

    }

    print(product_quantity)


    return context