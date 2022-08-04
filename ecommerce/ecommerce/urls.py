from django.contrib import admin
from django.urls import path
from ecommerce.ecommerce.views import products
from products.views import familia


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name='familia')
]