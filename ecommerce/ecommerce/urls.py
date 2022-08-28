from django.contrib import admin
from django.urls import path, include
from products.views import products
from ecommerce.views import products, index, about

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('products/', include('products.urls')),
    path('users/', include('users.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)