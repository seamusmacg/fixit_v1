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


def add_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart =  request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)