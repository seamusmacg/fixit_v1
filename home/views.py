from django.shortcuts import render

# Create your views here.

def index(request):
    """View that returns index page

    Args:
        request (request): HTTP request

    Returns:
        file: Index html file 
    """
    
    return render(request, 'home/index.html')