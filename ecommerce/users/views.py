from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form, UserEditForm

from users.models import User_profile

from django.contrib.auth.decorators import login_required


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'Users/login.html', {'error': 'Username o Password Invalido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)
    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})



def show_profile(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.profile) 

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserEditForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.password1 = data['password1']
            user.password2 = data['password2']
            user.save()
            return render(request,'index.html')
    else:
        user_form = UserEditForm(initial={'email': user.email })
    
    return render(request, 'users/edit_profile.html', {'user_form': user_form, 'user': user})







          