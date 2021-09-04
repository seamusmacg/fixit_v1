from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    """View that returns cart page

    Args:
        request (GET): HTTP request for cart.html

    Returns:
        HTML file: cart HTML file 
    """
    
    return render(request, 'cart/cart.html')


def add_cart(request, product_id):
    """View that adds products to cart

    Args:
        request (POST): POST request with product data
        product_id (Number): ID (number) of product

    Returns:
        [GET request]: Redirects to current page
    """
    
    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart =  request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'{product.name} added to your cart')
    else:
        cart[product_id] = quantity
        messages.success(request, f'{product.name} added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_cart(request, product_id):

    product = Product.objects.get(pk=product_id)
    cart =  request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
        messages.success(request, f'{product.name} removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))