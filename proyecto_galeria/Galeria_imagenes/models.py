# Contenido actualizado de Galeria_imagenes/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ¡NUEVO MODELO!
class Comunidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=250)

    def __str__(self):
        return self.nombre

# MODELO MODIFICADO (antes Galeria_imagenes)
class Post(models.Model):
    # Relaciones
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.SET_NULL, null=True, blank=True)

    # Contenido del post
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) # Nuevo campo
    archivo = models.ImageField(upload_to='imagenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def es_reciente(self):
        return (timezone.now() - self.fecha_creacion).days < 1

    def __str__(self):
        return f'"{self.titulo}" por {self.autor.username}'