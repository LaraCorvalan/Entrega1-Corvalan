from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor, Libro, Reseña
from myApp.forms import FormLibros, FormAutor, FormReseña
# Create your views here.


def inicio(request):
    posts = Libro.objects.all()
    return render(request, 'padre.html', {'posts': posts})


def about(request):
    return render(request, 'sobremi.html')


def formLibros(request):
    if request.method == 'POST':
        mi_formulario = FormLibros(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            libro = Libro(titulo=info['titulo'], autor=info['autor'], fecha_publicacion=info['fecha_publicacion'], paginas=info['paginas'], sinopsis=info['sinopsis'], genero=info['genero'])
            libro.save()
            return render(request, 'padre.html')
    else:
        mi_formulario = FormLibros()
        return render(request, 'formLibros.html', {'formulario':mi_formulario})   

def mostrarLibros(request):
    posts = Libro.objects.all()
    print(posts)
    return render(request, 'posts.html', {'posts': posts})


def formAutor(request):
    if request.method == 'POST':
        mi_formulario = FormAutor(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            autor = Autor(nombre=info['nombre'], biografia=info['biografia'], libros=info['libros'])
            autor.save()
            return render(request, 'padre.html')
    else:
        mi_formulario = FormAutor()
        return render(request, 'formAutor.html', {'formulario':mi_formulario})   

def formReseñas(request):
    if request.method == 'POST':
        mi_formulario = FormReseña(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            reseña = Reseña(libro=info['libro'], reseña=info['reseña'], estrellas=info['estrellas'])
            reseña.save()
            return render(request, 'padre.html')
    else:
        mi_formulario = FormReseña()
        return render(request, 'formReseñas.html', {'formulario':mi_formulario})   

def busqueda(request):
    return render(request, 'posts.html')

def search(request):
    if  request.GET["titulo"]:
        titulo= request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains = titulo)
        return render(request, 'results.html', {'libros': libros, 'titulo':titulo})
    else: 
        respuesta = 'No se encontró tu búsqueda'
    return HttpResponse(respuesta)


def reseñas(request):
    reseñas = Reseña.objects.all()
    return render(request, 'reseñas.html', {'reseñas': reseñas})