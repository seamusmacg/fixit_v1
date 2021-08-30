from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """View that returns cart page

    Args:
        request (GET): HTTP request for cart.html

    Returns:
        HTML file: cart HTML file 
    """
    
    return render(request, 'cart/cart.html')