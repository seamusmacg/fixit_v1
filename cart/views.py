from django.shortcuts import render, redirect

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

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart =  request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)