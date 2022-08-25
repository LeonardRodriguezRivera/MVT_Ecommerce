from django import forms

class Formulario_productos(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    stock = forms.IntegerField()
    email = forms.EmailField()

class Formulario_shop(forms.Form):   
    name = forms.CharField()
    location = forms.CharField()
    email = forms.EmailField()

class Formulario_distributor(forms.Form): 
    name = forms.CharField()
    zone = forms.CharField()
    email = forms.EmailField() 
 
