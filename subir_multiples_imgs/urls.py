from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("upload/", views.guardarMultiplesImgs, name="guardarMultiplesImgs"),
    path('listar-imagenes/', views.listarImagenes, name='listar_imagenes'),
]
