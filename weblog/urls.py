
from django.contrib import admin
from django.urls import path
# from . import views
from .views import MainWeBlog, WeBlogDetail, AddWeBlog, EditWeBlog, DeleteWeBlog

urlpatterns = [
    path('', MainWeBlog.as_view(), name="weblog"),
    path('article/<int:pk>', WeBlogDetail.as_view(), name="weblog-detail"),
    path('write_blog/', AddWeBlog.as_view(), name="write-weblog"),
    path('article/edit/<int:pk>', EditWeBlog.as_view(), name="edit-weblog"),
    path('article/<int:pk>/delete', DeleteWeBlog.as_view(), name="delete-weblog"),
   
]
