from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('cart/', views.cart, name='cart'),

    # path('seachResult/', views.seachResult, name='seachResult'),
]
