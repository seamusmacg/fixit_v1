from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
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
    



