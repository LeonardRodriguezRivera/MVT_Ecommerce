from multiprocessing import context
from django.shortcuts import render
from products.models import Products


def products(request):
    products = Products.objects.all()
    context = {

        'products': products
    }


    return render(request,'products.html', context=context)









#def products(request):
    #return HttpResponse("Hola productos")