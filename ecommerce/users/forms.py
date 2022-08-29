from socket import fromshare
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:'' for k in fields} 



class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = "Modificar email", required=False)
    first_name = forms.CharField(label = 'Agregar nombre', required=False)   
    last_name = forms.CharField(label = 'Agregar apellido', required=False)
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label = 'Password confirmation', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2' )
        help_texts = {k:'' for k in fields}
    

