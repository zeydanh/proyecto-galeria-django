# proyecto_galeria/Galeria_imagenes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from .forms import PostForm, UserRegisterForm, ComentarioForm
from .models import Post, Comunidad, Voto, Comentario

def inicio(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    comunidades = Comunidad.objects.all()
    contexto = {'posts': posts, 'comunidades': comunidades}
    return render(request, 'inicio.html', contexto)

def comunidad_detail(request, comunidad_nombre):
    comunidad = get_object_or_404(Comunidad, nombre=comunidad_nombre)
    posts = Post.objects.filter(comunidad=comunidad).order_by('-fecha_creacion')
    comunidades = Comunidad.objects.all()
    contexto = {
        'comunidad': comunidad,
        'posts': posts,
        'comunidades': comunidades
    }
    return render(request, 'comunidad_detail.html', contexto)

def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    posts = Post.objects.filter(autor=usuario).order_by('-fecha_creacion')
    contexto = {
        'usuario': usuario,
        'posts': posts,
    }
    return render(request, 'perfil.html', contexto)

@login_required
def votar(request, post_id, valor):
    post = get_object_or_404(Post, pk=post_id)
    valor_voto = 1 if valor == 'positivo' else -1
    voto_existente = Voto.objects.filter(usuario=request.user, post=post).first()

    if voto_existente:
        if voto_existente.valor == valor_voto:
            voto_existente.delete()
        else:
            voto_existente.valor = valor_voto
            voto_existente.save()
    else:
        Voto.objects.create(usuario=request.user, post=post, valor=valor_voto)
    
    # Responder a solicitudes de JavaScript
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'total_votos': post.total_votos})
    
    return redirect(request.META.get('HTTP_REFERER', 'inicio'))

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comentarios = post.comentarios.all()
    comentario_form = ComentarioForm()

    if request.method == 'POST':
        # Procesar comentario enviado con JavaScript
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                contenido = data.get('contenido', '')
                if contenido:
                    comentario = Comentario.objects.create(
                        post=post,
                        autor=request.user,
                        contenido=contenido
                    )
                    return JsonResponse({
                        'id': comentario.id,
                        'autor': comentario.autor.username,
                        'contenido': comentario.contenido,
                        'fecha_creacion': comentario.fecha_creacion.strftime('%d de %b, %Y'),
                        'total_comentarios': post.total_comentarios
                    })
                return JsonResponse({'error': 'El contenido no puede estar vacío'}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)

        # Procesamiento normal del formulario (si JavaScript falla)
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.autor = request.user
            nuevo_comentario.save()
            return redirect('post_detail', post_id=post.id)

    contexto = {
        'post': post,
        'comentarios': comentarios,
        'comentario_form': comentario_form,
    }
    return render(request, 'post_detail.html', contexto)

# --- FUNCIÓN RESTAURADA ---
@login_required
def registrar_imagen(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.autor = request.user
            nuevo_post.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'registrar.html', {'form': form})

# --- FUNCIÓN RESTAURADA ---
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