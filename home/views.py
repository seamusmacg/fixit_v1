from django.shortcuts import render

# Create your views here.

def index(request):
    """View that returns index page

    Args:
        request (GET): HTTP request for index.html

    Returns:
        HTML file: Index HTML file 
    """
    
    return render(request, 'home/index.html')