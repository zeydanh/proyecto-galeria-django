# Galeria_imagenes/views_api.py
from rest_framework import viewsets, permissions
from .models import Post, Comunidad, Comentario
from .serializers import PostSerializer, ComunidadSerializer, ComentarioSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar posts.
    """
    queryset = Post.objects.all().order_by('-fecha_creacion')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos por los que se puede filtrar, ej: /api/posts/?comunidad=1
    filterset_fields = ['comunidad', 'autor']

    # Campos por los que se puede buscar, ej: /api/posts/?search=Título
    search_fields = ['titulo', 'descripcion', 'autor__username']

    # Campos por los que se puede ordenar, ej: /api/posts/?ordering=total_votos
    ordering_fields = ['fecha_creacion', 'total_votos']

class ComunidadViewSet(viewsets.ModelViewSet):
    queryset = Comunidad.objects.all()
    serializer_class = ComunidadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]