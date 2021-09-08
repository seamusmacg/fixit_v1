from django.shortcuts import render

# Create your views here.

def get_profile(request):
    template = "profiles/profile.html"
    context = {}

    return render(request, template, context)
