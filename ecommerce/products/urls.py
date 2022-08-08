from django.contrib import admin
from django.urls import path
from products.views import products, distributor, shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name='products'), 
    path('distributor/', distributor, name='distributor'),
    path('shop/', shop, name='shop')
]