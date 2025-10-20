from rest_framework import serializers
from .models import Post, Comentario, Comunidad, Voto
from django.contrib.auth.models import User

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = ['id', 'nombre', 'descripcion']

class PostSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    comunidad = ComunidadSerializer(read_only=True)
    total_votos = serializers.IntegerField(read_only=True)
    total_comentarios = serializers.IntegerField(read_only=True)

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
            'autor_id', 'comunidad_id'
        ]

    def validate_titulo(self, value):
        palabras_prohibidas = ['spam', 'publicidad', 'oferta', 'gratis']
        titulo_limpio = value.lower()
        for palabra in palabras_prohibidas:
            if palabra in titulo_limpio:
                raise serializers.ValidationError(f"El título no puede contener la palabra '{palabra}'.")
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres.")
        return value

class ComentarioSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)

    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='autor', write_only=True,
        help_text="ID del usuario que crea el comentario."
    )
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post', write_only=True,
        help_text="ID del post que se está comentando."
    )

    class Meta:
        model = Comentario
        fields = [
            'id', 'post_id', 'autor', 'contenido', 'fecha_creacion',
            'autor_id'
        ]
        read_only_fields = ['id', 'autor', 'fecha_creacion']

    def validate(self, data):
        if data['post'].autor == data['autor']:
            raise serializers.ValidationError("Regla de negocio: No puedes comentar en tu propio post.")
        if len(data['contenido']) < 2:
            raise serializers.ValidationError("El comentario debe tener al menos 2 caracteres.")
        return data