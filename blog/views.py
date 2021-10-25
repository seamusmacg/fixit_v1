from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

# def blog(request):
#     return render(request, 'blog/blog.html')

class MainBlog(ListView):
    model = BlogPost
    template_name = 'blog/blog.html'
    ordering = ['-created_date']


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class AddBlog(CreateView):
    model = BlogPost
    template_name = 'blog/write_blog.html'
    fields = '__all__'


class EditBlog(UpdateView):
    model = BlogPost
    template_name = 'blog/edit_blog.html'
    fields = '__all__'


class DeleteBlog(DeleteView):
    model = BlogPost
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
    



