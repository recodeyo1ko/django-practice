from django.shortcuts import render
from .models import Category
from .models import Item
from django.db.models import Q

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'shopping/main.html', {'categories': categories})

def search(request):
    search_category = request.GET.get('search_category')
    search_name = request.GET.get('search_name', '')

    if search_category and search_category != '0':
        items = Item.objects.filter(
            Q(category__id=search_category) & 
            Q(name__icontains=search_name)
        )
    else:
        items = Item.objects.filter(name__icontains=search_name)
    
    categories = Category.objects.all()
    
    return render(request, 'shopping/searchResult.html', {
        'items': items,
        'search_name': search_name,
        'search_category': search_category,
        'categories': categories
    })

def cart(request):
    return render(request, 'shopping/cart.html')

def itemDetail(request):
    return render(request, 'shopping/itemDetail.html')

