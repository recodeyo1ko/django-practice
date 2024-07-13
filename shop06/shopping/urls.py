from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shopping'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('addToCart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),

    # path('seachResult/', views.seachResult, name='seachResult'),
]
