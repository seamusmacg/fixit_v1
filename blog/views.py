from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.

# def blog(request):
#     return render(request, 'blog/blog.html')

class MainBlog(ListView):
    model = BlogPost
    template_name = 'blog/blog.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'