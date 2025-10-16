# proyecto_galeria/Galeria_imagenes/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comunidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=250)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.ImageField(upload_to='imagenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def total_votos(self):
        return Voto.objects.filter(post=self).aggregate(total=models.Sum('valor'))['total'] or 0

    @property
    def total_comentarios(self):
        return self.comentarios.count()

    def __str__(self):
        return f'"{self.titulo}" por {self.autor.username}'

class Voto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votos')
    valor = models.IntegerField(choices=[(1, 'Positivo'), (-1, 'Negativo')])

    class Meta:
        unique_together = ('usuario', 'post')

    def __str__(self):
        return f'{self.usuario.username} votó {self.get_valor_display()} en "{self.post.titulo}"'

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'Comentario de {self.autor.username} en "{self.post.titulo}"'