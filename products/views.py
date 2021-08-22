from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.contrib import messages 
from django.db.models import Q

# Create your views here.

def get_products(request):
    """A view that returns products page with all product data.

    Args:
        request (GET): HTTP request for products.html

    Returns:
        HTML file: Products HTML file 
    """

    query = ""

    if request.method == "GET":
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Nothing entered into searchbar!")
                return redirect(reverse('products'))

        products = get_search_queries(query)

    context = {
        'products': products, 
        'search_term': query,
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


def get_search_queries(query=None):
    products = Product.objects.all()
    queries = Q(name__icontains=query) | Q(description__icontains=query) 

    products = products.filter(queries).distinct()

    return products

