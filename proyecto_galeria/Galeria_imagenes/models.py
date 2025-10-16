from django.db import models
from django.contrib.auth.models import User

class Galeria_imagenes(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to='imagenes/')
    fecha = models.DateTimeField(auto_now_add=True)
    
    @property
    def es_reciente(self):
        from django.utils import timezone
        return (timezone.now() - self.fecha).days < 1
    
    def __str__(self):
        return self.titulo