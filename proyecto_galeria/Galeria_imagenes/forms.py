from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# CORRECCIÓN: Importar solo el modelo 'Post'
from .models import Post

# Forma NUEVA Y ÚNICA para subir imágenes (ahora posts)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'comunidad', 'archivo']
        labels = {
            'titulo': 'Título del post',
            'descripcion': 'Descripción (opcional)',
            'comunidad': 'Elige una comunidad (opcional)',
            'archivo': 'Seleccionar imagen'
        }

# El formulario de registro de usuario se mantiene igual
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar mensajes de error y ayuda para contraseña
        self.fields['password1'].help_text = """
        <ul>
            <li>Su contraseña no puede ser demasiado similar a su otra información personal.</li>
            <li>Su contraseña debe contener al menos 8 caracteres.</li>
            <li>Su contraseña no puede ser una contraseña de uso común.</li>
            <li>Su contraseña no puede ser enteramente numérica.</li>
        </ul>
        """
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user