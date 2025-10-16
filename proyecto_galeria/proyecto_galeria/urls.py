# proyecto_galeria/proyecto_galeria/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importaciones necesarias para la API y su documentación
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # URLs existentes
    path('admin/', admin.site.urls),
    path('', include('Galeria_imagenes.urls')), # URLs de tu aplicación web

    # --- NUEVAS URLS PARA LA API, AUTENTICACIÓN Y DOCUMENTACIÓN ---

    # 1. Incluye las URLs de tu API (posts, comentarios, etc.)
    #    Esto le dice a Django que busque las rutas que empiezan con 'api/'
    #    en el archivo 'Galeria_imagenes.api_urls'.
    path('api/', include('Galeria_imagenes.api_urls')),

    # 2. Endpoints para la autenticación con tokens JWT.
    #    Permitirá a los usuarios obtener y refrescar tokens de acceso.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 3. Endpoints para la documentación automática de la API (Swagger UI).
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

# Esto se mantiene igual para servir archivos de medios (imágenes) en modo de desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)