from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import PostForm, UserRegisterForm
from .models import Post

def inicio(request):
    # Lógica actualizada: Obtener todos los Posts y ordenarlos por fecha
    posts = Post.objects.all().order_by('-fecha_creacion')
    # Pasar los 'posts' a la plantilla
    return render(request, 'inicio.html', {'posts': posts})

@login_required
def registrar_imagen(request):
    if request.method == 'POST':
        # Usar el nuevo PostForm
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Lógica actualizada: No guardar inmediatamente
            nuevo_post = form.save(commit=False)
            # Asignar el usuario actual como el autor
            nuevo_post.autor = request.user
            # Ahora sí, guardar el post con su autor
            nuevo_post.save()
            return redirect('inicio')
    else:
        # Usar el nuevo PostForm
        form = PostForm()
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
def post_detail(request, post_id):
    # Busca el post por su ID. Si no lo encuentra, muestra un error 404.
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})