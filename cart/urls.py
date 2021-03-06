from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<product_id>/', views.add_cart, name="add_cart"),
    path('remove/<product_id>/', views.remove_cart, name="remove_cart"),
]
