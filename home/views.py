from django.shortcuts import render
from django.contrib import messages 
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.


@xframe_options_exempt
def index(request):
    """View that returns index page

    Args:
        request (GET): HTTP request for index.html

    Returns:
        HTML file: Index HTML file 
    """
    
    return render(request, 'home/index.html')


def contact(request):
    """View that returns contact page

    Args:
        request (GET): HTTP request for contact.html

    Returns:
        HTML file: contact HTML file 
    """

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        question = request.POST['question']
        if name == "" or email == "" or question == "":
            messages.warning(request, "There is one or more empty fields - cannot be empty!")
        else:
            return render(request, 'home/success.html')

  
    return render(request, 'home/contact.html')

