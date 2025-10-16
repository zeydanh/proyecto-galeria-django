# Galeria_imagenes/admin.py

from django.contrib import admin
# CORRECCIÓN: Importar Post y Comunidad, no Galeria_imagenes
from .models import Post, Comunidad 

admin.site.register(Post)
admin.site.register(Comunidad)