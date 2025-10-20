# proyecto_galeria/Galeria_imagenes/admin.py

from django.contrib import admin
from .models import Post, Comunidad, Voto, Comentario

admin.site.register(Post)
admin.site.register(Comunidad)
admin.site.register(Voto)
admin.site.register(Comentario)