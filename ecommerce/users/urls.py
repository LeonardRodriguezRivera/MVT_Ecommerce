from django.urls import path
from users.views import login_request, register, logout


urlpatterns=[
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]