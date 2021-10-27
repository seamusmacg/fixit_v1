from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

class MainWeBlog(ListView):
    model = Post
    template_name = 'weblog/weblog.html'
    ordering = ['-created_date']


class WeBlogDetail(DetailView):
    model = Post
    template_name = 'weblog/weblog_detail.html'


class AddWeBlog(CreateView):
    model = Post
    template_name = 'weblog/write_weblog.html'
    fields = '__all__'


class EditWeBlog(UpdateView):
    model = Post
    template_name = 'weblog/edit_weblog.html'
    fields = '__all__'


class DeleteWeBlog(DeleteView):
    model = Post
    template_name = 'weblog/delete_weblog.html'
    success_url = reverse_lazy('weblog')


class Categories(ListView):
    model = Category
    template_name = 'weblog/categories.html'


class AddCategory(CreateView):
    model = Category
    template_name = 'weblog/add_category.html'
    fields = '__all__'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'weblog/category_detail.html'


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'weblog/delete_category.html'
    success_url = reverse_lazy('categories')
    



