from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import AgregarUsuario, Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('gestionarUsuarios')
    else:
        return redirect('login')

def salir(request):
    logout(request)
    return redirect('/')
    
@login_required(login_url='login')
def gestionarUsuarios(request):
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        regDB.save()
    usuarios=User.objects.all()
    form=AgregarUsuario()
    return render(request,"GestionarUsuarios.html",{'form':form,'usuarios':usuarios,})

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('gestionarUsuarios')
    return render(request,"login.html",{'form':form,})

