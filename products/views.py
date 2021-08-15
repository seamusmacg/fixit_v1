from django.shortcuts import render
from .models import Product

# Create your views here.

def get_products(request):
    """A view that returns product page with product data.

    Args:
        request (GET): HTTP request for products.html

    Returns:
        HTML file: Products HTML file 
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)