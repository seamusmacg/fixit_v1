
from django.contrib import admin
from django.urls import path
# from . import views
from .views import MainBlog, BlogDetail, AddBlog

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', MainBlog.as_view(), name="blog"),
    path('article/<int:pk>', BlogDetail.as_view(), name="blog-detail"),
    path('write_blog/', AddBlog.as_view(), name="write-blog"),
   
]
