from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('c/<str:comunidad_nombre>/', views.comunidad_detail, name='comunidad_detail'),
    path('u/<str:username>/', views.perfil_usuario, name='perfil'),
    path('post/<int:post_id>/votar/<str:valor>/', views.votar, name='votar'),
    path('registrar/', views.registrar_imagen, name='registrar_imagen'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registrar_usuario, name='registro'),
]