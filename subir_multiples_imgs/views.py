from django.shortcuts import render, redirect
import uuid


# Create your views here.
from .models import Galeria


def inicio(request):
    return render(request, 'index.html')


def guardarMultiplesImgs(request):
    context = {}  # Inicializar context aquí

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

        uploaded_images = Galeria.objects.all()
        context = {'data': uploaded_images}

    return render(request, "index.html", context)


def listarImagenes(request):
    uploaded_images = Galeria.objects.all()
    context = {'data': uploaded_images}
    return render(request, "listar_imagenes.html", context)
