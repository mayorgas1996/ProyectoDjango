from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', {
        'title':'Inicio'
    })

def about(request):
    return render(request, 'main_app/about.html', {
        'title':'Sobre nosotros'
    })

def register_page(request):

    register_form = UserCreationForm()

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)

        #Se guarda el usuario
        if register_form.is_valid():
            register_form.save()

            return redirect('inicio')


    return render(request, 'users/register.html',{
        'title':'Registro',
        'register_form': register_form
    })