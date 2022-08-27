from http.client import HTTPResponse
from multiprocessing import context
import pkgutil
from django.shortcuts import render, redirect
from products.models import Products, Shop, Distributor
from products.forms import Formulario_productos, Formulario_shop, Formulario_distributor

from django.views.generic import DetailView


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
                email = form.cleaned_data['email'],
                stock = form.cleaned_data['stock']
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


def delete_product(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'delete_product.html', context=context)
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(products)


def delete_distributor(request, pk):
    if request.method == 'GET':
        distribut = Distributor.objects.get(pk=pk)
        context = {'distribut': distribut}
        return render(request, 'delete_distributor.html', context=context)
    elif request.method == 'POST':
        distribut = Distributor.objects.get(pk=pk)
        distribut.delete()
        return redirect(distributor)


def delete_shop(request, pk):
    if request.method == 'GET':
        business = Shop.objects.get(pk=pk)
        context = {'business': business}
        return render(request, 'delete_shop.html', context=context)
    elif request.method == 'POST':
        business = Shop.objects.get(pk=pk)
        business.delete()
        return redirect(shop)


    
    
def update_product(request, pk):
    if request.method == 'POST':
        form = Formulario_productos(request.POST)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.stock = form.cleaned_data['stock']
            product.email = form.cleaned_data['email']
            product.save()
            return redirect(products)
    elif request.method == 'GET':
        product = Products.objects.get(id=pk)
        form = Formulario_productos(initial= {
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'email': product.email
        })
        context = {'form': form}
        return render(request, 'update_product.html', context=context)


# Vista Detalle a partir de clase

class Details_product(DetailView):
     model = Products
     template_name = 'details_products.html'


