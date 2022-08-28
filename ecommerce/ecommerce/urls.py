from django.contrib import admin
from django.urls import path, include
from products.views import products
from ecommerce.views import products, index, about, error_404

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('products/', include('products.urls')),
    path('users/', include('users.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error_404.as_view()