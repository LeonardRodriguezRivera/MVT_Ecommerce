from django.contrib import admin
from django.urls import path, include
from products.views import products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products),
    path('products/', include('products.urls'))
]