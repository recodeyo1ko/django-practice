from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'shopping/cart.html')

def itemDetail(request):
    return render(request, 'shopping/itemDetail.html')

def main(request):
    return render(request, 'shopping/main.html')

def seachResult(request):
    return render(request, 'shopping/seachResult.html')