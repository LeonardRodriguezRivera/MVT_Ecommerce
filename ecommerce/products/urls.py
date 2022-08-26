from django.contrib import admin
from django.urls import path
from products.views import products, distributor, shop, create_product, create_shop, create_distributor, search_products, delete_product


urlpatterns = [ 
    path('products/', products, name='products'), 
    path('distributor/', distributor, name='distributor'),
    path('shop/', shop, name='shop'),
    path('create-product/', create_product, name='create_product'),
    path('create-shop/', create_shop, name='create_shop'),
    path('create-distributor/', create_distributor, name='create_distributor'),
    path('search-products/', search_products, name= 'search_products'),
    path('delete-product/<int:pk>/', delete_product, name= 'delete_product') 
]