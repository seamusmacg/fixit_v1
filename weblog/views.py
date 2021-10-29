from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminStaffOnly(LoginRequiredMixin, UserPassesTestMixin):
    """Class the makes other classes only apply to superusers"""

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class MainWeBlog(ListView):
    """Class to display main blog page"""
    model = Post
    template_name = 'weblog/weblog.html'
    ordering = ['-created_date']


class WeBlogDetail(DetailView):
    """Class to display blog detail page"""
    model = Post
    template_name = 'weblog/weblog_detail.html'


class AddWeBlog(AdminStaffOnly, CreateView):
    """Class to display and post write blog page"""
    model = Post
    template_name = 'weblog/write_weblog.html'
    fields = '__all__'


class EditWeBlog(AdminStaffOnly, UpdateView):
    """Class to display and post edit blog page"""
    model = Post
    template_name = 'weblog/edit_weblog.html'
    fields = '__all__'


class DeleteWeBlog(AdminStaffOnly, DeleteView):
    """Class to display and post delete blog page"""
    model = Post
    template_name = 'weblog/delete_weblog.html'
    success_url = reverse_lazy('weblog')


class Categories(ListView):
    """Class to display categories page"""
    model = Category
    template_name = 'weblog/categories.html'


class AddCategory(AdminStaffOnly, CreateView):
    """Class to display and post add category page"""
    model = Category
    template_name = 'weblog/add_category.html'
    fields = '__all__'


class CategoryDetail(DetailView):
    """Class to display category detail page"""
    model = Category
    template_name = 'weblog/category_detail.html'


class DeleteCategory(AdminStaffOnly, DeleteView):
    """Class to display and post delete category page"""
    model = Category
    template_name = 'weblog/delete_category.html'
    success_url = reverse_lazy('categories')
