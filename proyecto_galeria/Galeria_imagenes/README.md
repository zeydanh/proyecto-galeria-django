# Proyecto Galería API - KoyPics

API RESTful desarrollada con Django y Django REST Framework que permite gestionar una galería de imágenes con posts, comunidades, comentarios y votos.

## Requisitos

* Python 3.8+
* pip

## Instalación

1.  **Clonar el repositorio o descomprimir el archivo .zip**
    ```bash
    git clone <tu-repositorio>
    cd proyecto-galeria-django
    ```

2.  **Crear y activar un entorno virtual**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar las dependencias**
    Para este proyecto, se necesitan las siguientes dependencias. Puedes crear un archivo `requirements.txt` con este contenido y luego instalarlo.

    **requirements.txt:**
    ```
    Django
    djangorestframework
    djangorestframework-simplejwt
    django-filter
    drf-spectacular
    ```

    Instala las dependencias con:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar las migraciones**
    Esto creará la base de datos `db.sqlite3` y las tablas necesarias.
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario**
    Necesitarás un superusuario para acceder al panel de administración y para obtener tokens de autenticación fácilmente.
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear tu usuario (nombre, email y contraseña).

6.  **Iniciar el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```
    El servidor estará disponible en `http://127.0.0.1:8000/`.

## Cómo Probar la API

### 1. Obtener Token de Autenticación (JWT)

Para interactuar con los endpoints protegidos, primero necesitas un token de acceso.

* **Endpoint:** `POST /api/token/`
* **Body (JSON):**
    ```json
    {
        "username": "tu-superusuario",
        "password": "tu-contraseña"
    }
    ```
* **Respuesta Exitosa:**
    ```json
    {
        "refresh": "eyJhbGciOiJIUz...",
        "access": "eyJhbGciOiJIUz..."
    }
    ```
Copia el token `access`. Lo necesitarás para las siguientes peticiones.

### 2. Probar el CRUD

En tus herramientas de cliente API (como Postman, Insomnia o curl), añade el siguiente encabezado a tus peticiones:

`Authorization: Bearer <tu-token-access>`

A continuación, algunos ejemplos de endpoints que puedes probar:

* **Listar todos los Posts (GET):** `http://127.0.0.1:8000/api/posts/`
* **Crear un nuevo Post (POST):** `http://127.0.0.1:8000/api/posts/`
    * **Body (form-data):** `titulo`, `descripcion`, `archivo` (subir una imagen), `autor_id` (el ID de tu superusuario), `comunidad_id` (opcional).
* **Obtener un Post específico (GET):** `http://127.0.0.1:8000/api/posts/1/`
* **Actualizar un Post (PUT/PATCH):** `http://127.0.0.1:8000/api/posts/1/`
* **Eliminar un Post (DELETE):** `http://127.0.0.1:8000/api/posts/1/`

Puedes hacer lo mismo para los endpoints de `comunidades` y `comentarios`.

### 3. Acceder a la Documentación de la API

La API está completamente documentada usando OpenAPI y puede ser explorada a través de Swagger UI.

* **Schema (JSON):** [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)
* **Swagger UI (Interfaz Gráfica):** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

Desde la interfaz de Swagger, puedes probar todos los endpoints de forma interactiva, incluyendo la autorización.