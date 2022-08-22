from django.contrib import admin
from django.urls import path, include
from products.views import products
from ecommerce.views import products, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]