
from django.contrib import admin
from django.urls import path
# from . import views
from .views import MainBlog, BlogDetail, AddBlog, EditBlog

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', MainBlog.as_view(), name="blog"),
    path('article/<int:pk>', BlogDetail.as_view(), name="blog-detail"),
    path('write_blog/', AddBlog.as_view(), name="write-blog"),
    path('article/edit/<int:pk>', EditBlog.as_view(), name="edit-blog"),
   
]
