from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
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

    products = Product.objects.all()
    query = ""
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            products = get_product_queries(query)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': current_sorting,
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


def get_product_queries(query=None):
    products = Product.objects.all()
    queries = Q(name__icontains=query) | Q(description__icontains=query) 

    products = products.filter(queries).distinct()

    return products








