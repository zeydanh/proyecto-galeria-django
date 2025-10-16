# Galeria_imagenes/api_urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views_api import PostViewSet, ComunidadViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comunidades', ComunidadViewSet, basename='comunidad')
router.register(r'comentarios', ComentarioViewSet, basename='comentario')

urlpatterns = [
    path('', include(router.urls)),
]