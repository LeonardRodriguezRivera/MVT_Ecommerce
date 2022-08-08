from multiprocessing import context
from django.shortcuts import render
from products.models import Products, Shop, Distributor


def products(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request,'products.html', context=context)

def distributor(request):
    distributor = Distributor.objects.all()
    context = {
        'distributor': distributor
    }
    return render(request,'distributor.html', context=context)

def shop(request):
    shop = Shop.objects.all()
    context = {
        'shop': shop
    }
    return render(request,'shop.html', context=context)    
    
    






