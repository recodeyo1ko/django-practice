from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .models import Item
from .models import ItemsInCart
from django.db.models import Q
from django.utils import timezone


# Create your views here.

def index(request):
    categories = Category.objects.all()
    is_login = request.session.get('is_login', None)
    context = {
        'categories': categories,
        'is_login': is_login
    }
    return render(request, 'shopping/main.html', context)

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

def item_detail(request, item_id):
  item = get_object_or_404(Item, item_id=item_id)
  return render(request, 'shopping/itemDetail.html', {'item': item})


def add_to_cart(request):
    if not request.session.get('is_login'):
        return redirect('account:login')
    item_id = request.POST.get('item_id')
    amount = request.POST.get('amount')

    if ItemsInCart.objects.filter(item_id=item_id).exists():
        items_in_cart = ItemsInCart.objects.get(item_id=item_id, user_id=request.session.get('user_id'))
        items_in_cart.amount += int(amount)
        items_in_cart.booked_date = timezone.now()
        items_in_cart.save()
    else:
        items_in_cart = ItemsInCart()
        items_in_cart.item = Item.objects.get(item_id=item_id)
        items_in_cart.amount = amount
        items_in_cart.booked_date = timezone.now()
        items_in_cart.user_id = request.session.get('user_id')
        items_in_cart.save()
    return redirect('shopping:cart')

def cart(request):
    cart_items = ItemsInCart.objects.all()
    return render(request, 'shopping/cart.html', {'cart_items': cart_items})