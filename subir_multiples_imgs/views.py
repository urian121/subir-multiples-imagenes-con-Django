from django.shortcuts import render, redirect
import uuid


# Create your views here.
from .models import Galeria


def inicio(request):
    context = {'data': listarImagenes(request)}
    return render(request, 'index.html', context)


def guardarMultiplesImgs(request):
    if request.method == "POST":
        # Obtener una lista de archivos adjuntos con el nombre "images"
        images = request.FILES.getlist('images')
        # Recorrer la lista de archivos adjuntos,
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
