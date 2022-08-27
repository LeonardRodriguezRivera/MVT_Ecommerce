from django.contrib import admin
from django.urls import path
from products.views import products, distributor, shop, create_product, create_shop, create_distributor, search_products, delete_product, update_product, delete_distributor, delete_shop, update_distributor, update_shop, Details_product, Details_distributor, Details_shop


urlpatterns = [ 
    path('products/', products, name='products'), 
    path('distributor/', distributor, name='distributor'),
    path('shop/', shop, name='shop'),
    path('create-product/', create_product, name='create_product'),
    path('create-shop/', create_shop, name='create_shop'),
    path('create-distributor/', create_distributor, name='create_distributor'),
    path('search-products/', search_products, name= 'search_products'),
    path('delete-product/<int:pk>/', delete_product, name= 'delete_product'),
    path('delete-shop/<int:pk>/', delete_shop, name= 'delete_shop'),
    path('delete-distributor/<int:pk>/', delete_distributor, name= 'delete_distributor'),
    path('update-product/<int:pk>/', update_product, name= 'update_product'),
    path('update-distributor/<int:pk>/', update_distributor, name= 'update_distributor'),
    path('update-shop/<int:pk>/', update_shop, name= 'update_shop'),
    path('details-product/<int:pk>/', Details_product.as_view(), name= 'Details_product'),
    path('details-distributor/<int:pk>/', Details_distributor.as_view(), name= 'Details_distributor'),
    path('details-shop/<int:pk>/', Details_shop.as_view(), name= 'Details_shop')    
]