from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('<product_id>', views.get_product, name='product_info'),
]