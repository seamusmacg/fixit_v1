
from django.contrib import admin
from django.urls import path
from .views import MainWeBlog, WeBlogDetail, AddWeBlog, EditWeBlog, DeleteWeBlog, AddCategory, CategoryDetail, DeleteCategory, Categories

urlpatterns = [
    path('', MainWeBlog.as_view(), name="weblog"),
    path('article/<int:pk>', WeBlogDetail.as_view(), name="weblog-detail"),
    path('write_blog/', AddWeBlog.as_view(), name="write-weblog"),
    path('article/edit/<int:pk>', EditWeBlog.as_view(), name="edit-weblog"),
    path('article/<int:pk>/delete', DeleteWeBlog.as_view(), name="delete-weblog"),
    path('categories/', Categories.as_view(), name="categories"),
    path('add_category/', AddCategory.as_view(), name="add-category"),
    path('category/<int:pk>', CategoryDetail.as_view(), name="category-detail"),
    path('category/delete/<int:pk>',
         DeleteCategory.as_view(), name="delete-category"),
]
