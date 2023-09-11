# Guardar archivo imagen en Django Python 🐍

###### 1. Crear un entorno virtual, hay muchas formas

Opción 1: Crear entorno virtual con el paquete virtualenv, puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
`	  
    pip install virtualenv
    virtualenv --version
    virtualenv env
`

Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
`python -m venv env`

###### 2. Activar ambiente virtual

    . env/Script/activate
    Para desactivar mi entorno virtual  ` deactivate`

###### 3. Instalar Djando desde el manejador de paquete de Python Pip

    pip install Django
    Nota: para instalar Django en una version especifica
    pip install Django==4.2.4

###### 4. Instalar el paquete (biblioteca) Pillow, esto con el fin de poder procesar la subida de imagen en el servidor

    Pillow es la librería que nos permitirá usar el campo ImageField para poder guardar imágenes

    - https://pypi.org/project/Pillow/
      pip install Pillow

###### 5. Crear el proyecto con Djando

    `django-admin startproject project_core .`
    El punto . es crucial le dice al script que instale Django en el directorio actual

     Ya en este punto se puede correr el proyecto que a creado Django,
      python manage.py runserver

###### 6. Crear mi primera aplicación en Django

    python manage.py startapp subir_multiples_imgs

###### 7. Crear el archivo requirements.txt para tener todos mis paquetes a la mano

    pip freeze > requirements.txt
    Nota: para instalar los paquetes solo basta ejecutar

###### 8. Instalar nuestra aplicación (subir_multiples_imgs) ya creada en el proyecto

    archivo settings.py
    INSTALLED_APPS = [
    ----,
    'subir_multiples_imgs',
    ]

##### 1. Configurar tu settings.py

    import os
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    IMPORTANTE: crear una carpeta al mismo nivel del proyecto 'project_core' que se llame 'media' sera alli donde
    guardaremos las imagenes subidas.

#### 2. Configurar tu archivo urls.py del proyecto

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    	# tus urls
    ]

    if settings.DEBUG:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#### 3. Definiendo tu models.py

    from django.db import models

    class Documento(models.Model):
        images = models.ImageField(upload_to='images/')
        created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

#### 5. Define tu views.py

    def inicio(request):
        context = {'data': listarImagenes(request)}
        return render(request, 'index.html', context)


    def guardarMultiplesImgs(request):
        if request.method == "POST":
            images = request.FILES.getlist('images')
            for image in images:
                # Obtener el nombre original del archivo
                original_filename = image.name
                # Generar un nuevo nombre de archivo con un UUID aleatorio
                unique_filename = str(uuid.uuid4()) + "_" + original_filename
                # Asignar el nuevo nombre al archivo
                image.name = unique_filename
                # Guardar la imagen en el sistema de archivos
                Galeria.objects.create(images=image)
        return redirect('inicio')


    def listarImagenes(request):
        return Galeria.objects.all()

#### Correr las migraciones

    python3 manager.py migrate

#### 6 Pintando el formulario en tu plantilla index.html

    <form
        action="{% url 'guardarMultiplesImgs' %}"
        method="POST"
        enctype="multipart/form-data">
        {% csrf_token %}
        <input type="file" name="images" accept="image/*" multiple />
        <button type="submit" class="btn btn-primary">
            Registrar imagenes
        </button>
    </form>

##### Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/Subir%20Multiples%20Imagenes%20con%20Django%20%20Python.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
