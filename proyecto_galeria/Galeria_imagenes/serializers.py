# Galeria_imagenes/serializers.py
from rest_framework import serializers
from .models import Post, Comentario, Comunidad, Voto
from django.contrib.auth.models import User

# Serializer para mostrar información básica del autor
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Serializer para mostrar información básica de la comunidad
class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = ['id', 'nombre']

# Serializer principal para el modelo Post
class PostSerializer(serializers.ModelSerializer):
    # Campos de solo lectura para mostrar información anidada
    autor = AutorSerializer(read_only=True)
    comunidad = ComunidadSerializer(read_only=True)
    total_votos = serializers.IntegerField(read_only=True)
    total_comentarios = serializers.IntegerField(read_only=True)

    # Campos de escritura que aceptan IDs
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='autor', write_only=True
    )
    comunidad_id = serializers.PrimaryKeyRelatedField(
        queryset=Comunidad.objects.all(), source='comunidad', write_only=True, required=False
    )

    class Meta:
        model = Post
        fields = [
            'id', 'titulo', 'descripcion', 'archivo', 'fecha_creacion',
            'autor', 'comunidad', 'total_votos', 'total_comentarios',
            'autor_id', 'comunidad_id' # Campos para la escritura
        ]

# Serializer para los comentarios
class ComentarioSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor', 'contenido', 'fecha_creacion']