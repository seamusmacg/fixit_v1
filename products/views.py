from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def get_products(request):
    """A view that returns products page with all product data.

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


def get_product(request, product_id):
    """A view that returns product page with product data.

    Args:
        request (GET): HTTP request for products.html

    Returns:
        HTML file: Products HTML file 
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)