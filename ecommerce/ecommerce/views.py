from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import DetailView


def products(request):
    return render(request,'products.html', context={})

def index(request):
     return render(request,'index.html')

def about(request):
     return render(request,'about.html')