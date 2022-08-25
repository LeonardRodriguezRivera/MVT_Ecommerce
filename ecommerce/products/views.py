from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from products.models import Products, Shop, Distributor
from products.forms import Formulario_productos, Formulario_shop, Formulario_distributor

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
    
def create_product(request): 

    if request.method == 'POST':
        form = Formulario_productos(request.POST)

        if form.is_valid():
            Products.objects.create(
                name= form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                email = form.cleaned_data['email']
            )
            return redirect(products)

    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'form':form}
        return render(request, 'creates/create_products.html', context=context) 



def create_shop(request): 

    if request.method == 'POST':
        form = Formulario_shop(request.POST)

        if form.is_valid():
            Shop.objects.create(
                name= form.cleaned_data['name'],
                location = form.cleaned_data['location'],
                email = form.cleaned_data['email']
            )
            return redirect(shop)

    elif request.method == 'GET':
        form = Formulario_shop()
        context = {'form':form}
        return render(request, 'creates/create_shop.html', context=context)         



def create_distributor(request): 

    if request.method == 'POST':
        form = Formulario_distributor(request.POST)

        if form.is_valid():
            Distributor.objects.create(
                name= form.cleaned_data['name'],
                zone = form.cleaned_data['zone'],
                email = form.cleaned_data['email']
            )
            return redirect(distributor)

    elif request.method == 'GET':
        form = Formulario_distributor()
        context = {'form':form}
        return render(request, 'creates/create_distributor.html', context=context)          


def search_products(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)
    context = {'products' : products}
    return render(request, 'search_products.html', context = context )