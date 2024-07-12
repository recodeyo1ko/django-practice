from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('itemDetail/', views.itemDetail, name='itemDetail'),
    # path('seachResult/', views.seachResult, name='seachResult'),
]
