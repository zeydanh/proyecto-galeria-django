# proyecto_galeria/Galeria_imagenes/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }
        labels = {
            'contenido': ''
        }

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
        self.fields['password1'].help_text = """
        <ul>
            <li>Su contraseña no puede ser demasiado similar a su otra informaciÃ³n personal.</li>
            <li>Su contraseña debe contener al menos 8 caracteres.</li>
            <li>Su contraseña no puede ser una contraseña de uso comÃºn.</li>
            <li>Su contraseña no puede ser enteramente numÃ©rica.</li>
        </ul>
        """
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user