from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import Galeria_imagenesForm, UserRegisterForm
from .models import Galeria_imagenes

def inicio(request):
    imagenes = Galeria_imagenes.objects.all()
    return render(request, 'inicio.html', {'imagenes': imagenes})

@login_required
def registrar_imagen(request):
    if request.method == 'POST':
        form = Galeria_imagenesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = Galeria_imagenesForm()
    return render(request, 'registrar.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})