from django.urls import path
from users.views import login_request, register, show_profile, edit_profile
from django.contrib.auth.views import LogoutView


urlpatterns=[
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view (template_name = 'users/logout.html') , name='logout'),
    path('profile/', show_profile , name='show_profile'),
    path('edite-profile/', edit_profile , name='edit_profile')
]